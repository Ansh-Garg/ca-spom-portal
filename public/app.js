/**
 * CA Final SPOM Intelligence Portal - Frontend Application Controller
 * High-Stakes Exam Testing Engine & Pedagogical Revision Platform
 *
 * Minimalist Luxury Aesthetic (Light Theme Default)
 * Strict Evaluation Across TOTAL Questions Perspective (100 Marks Benchmark)
 * 100% Option Shuffling Preservation from Test to Evaluation Sheet
 */

const app = {
  // Global State
  currentSet: 'A', // 'A' (Corporate & Economic Laws) or 'B' (SCPM)
  activeTab: 'home',
  currentMockMode: 'full_mock_50', // 'full_mock_50', 'full_mock_70', 'quick_blitz'
  currentHandbookCategory: 'summary', // 'summary', 'limits', 'confused', 'traps', 'intelligence'
  currentHandbookChapter: null,
  currentMistakeFilter: 'all', // 'all', 'unrevised', 'reviewed', 'mastered', 'starred'
  currentQBFilter: {
    set: 'all',
    chapter: 'all',
    source: 'all',
    section: 'all',
    search: ''
  },

  // Cached Data Repositories
  chapters: [],
  intelligenceDashboard: null,
  bookmarkedList: [],
  mistakesList: [],
  qbQuestions: [],

  // Intelligent Practice Engine State (10 Targeted Modes)
  // Chapter Selection Studio State
  selectedChapters: [],

  practiceState: {
    active: false,
    mode: 'mixed',
    chapterCode: null,
    count: 10,
    questions: [],
    currentIndex: 0,
    selectedOption: null,
    isAnswerChecked: false,
    score: 0,
    correctCount: 0,
    incorrectCount: 0,
    startTime: null
  },

  // Question Bank Coverage & Mastery Hub State
  coverageState: {
    data: null,
    selectedCohort: 'never_attempted', // 'never_attempted', 'wrong_many_times', 'correct_many_times', 'attempted'
    selectedChapter: 'all',
    activeSubtab: 'coverage'
  },

  // CBT Mock Simulator State (TCS iON Emulation)
  mockExam: {
    active: false,
    questions: [],
    currentIndex: 0,
    userResponses: {}, // q_id -> 'A', 'B', 'C', 'D'
    correctKeysMap: {}, // q_id -> shuffled_correct_key
    statuses: [],      // 'not-visited', 'not-answered', 'answered', 'marked-review', 'answered-marked'
    timeRemaining: 10800, // in seconds (180 mins)
    timerInterval: null,
    startTime: null,
    totalQuestions: 50,
    maxMarks: 100,
    currentSectionFilter: 'all' // 'all', 'Part I', 'Part II'
  },

  // Last Test Evaluation Record
  lastResult: null,

  // =========================================================================
  // Multi-Tenant Personal Workspace & Local Caching Engine
  // =========================================================================

  getUserId() {
    let uid = null;
    try {
      uid = localStorage.getItem('spom_uid');
    } catch (e) {}

    if (!uid) {
      const match = document.cookie.match(/(?:^|;\s*)spom_uid\s*=\s*([^;]+)/);
      if (match && match[1]) {
        uid = match[1].trim();
      }
    }

    if (!uid) {
      const rand = Math.random().toString(36).substring(2, 9);
      const ts = Date.now().toString(36);
      uid = `spom_u_${rand}${ts}`;
    }

    try {
      localStorage.setItem('spom_uid', uid);
    } catch (e) {}

    try {
      document.cookie = `spom_uid=${uid}; Path=/; Max-Age=315360000; SameSite=Lax`;
    } catch (e) {}

    return uid;
  },

  getCache(key) {
    try {
      const fullKey = `spom_cache_${this.getUserId()}_${key}`;
      const raw = localStorage.getItem(fullKey);
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      return parsed.data;
    } catch (e) {
      return null;
    }
  },

  setCache(key, data) {
    try {
      const fullKey = `spom_cache_${this.getUserId()}_${key}`;
      const item = {
        timestamp: Date.now(),
        data: data
      };
      localStorage.setItem(fullKey, JSON.stringify(item));
    } catch (e) {}
  },

  clearUserCache() {
    try {
      const prefix = `spom_cache_${this.getUserId()}_`;
      const toRemove = [];
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith(prefix)) {
          toRemove.push(k);
        }
      }
      toRemove.forEach(k => localStorage.removeItem(k));
    } catch (e) {}
  },

  async apiFetch(url, options = {}) {
    const uid = this.getUserId();
    const headers = Object.assign({}, options.headers || {});
    headers['X-User-ID'] = uid;

    if (options.body && typeof options.body === 'object' && !(options.body instanceof FormData)) {
      headers['Content-Type'] = headers['Content-Type'] || 'application/json';
      options.body = JSON.stringify(options.body);
    }

    return await fetch(url, {
      ...options,
      headers,
      credentials: 'same-origin'
    });
  },

  updateWorkspaceUI() {
    const uid = this.getUserId();
    const dispEl = document.getElementById('user-id-display');
    const fullEl = document.getElementById('workspace-id-full');
    if (dispEl) dispEl.textContent = 'Workspace';
    if (fullEl) fullEl.textContent = uid;
  },

  openWorkspaceModal() {
    const modal = document.getElementById('workspace-modal');
    if (modal) {
      this.updateWorkspaceUI();
      modal.classList.add('active');
    }
  },

  closeWorkspaceModal() {
    const modal = document.getElementById('workspace-modal');
    if (modal) {
      modal.classList.remove('active');
    }
  },

  async resetUserWorkspace() {
    const confirmed = confirm(
      "Reset Workspace Progress?\n\nThis will clear your 100 Marks mock exam attempts, Mistakes Book records, and Question Bank coverage history.\n\nOther students' progress will NOT be affected. Are you sure you want to proceed?"
    );
    if (!confirmed) return;

    try {
      this.showToast("Resetting your personal workspace...", 'info');
      const res = await this.apiFetch('/api/user/reset', { method: 'POST' });
      const data = await res.json();
      if (data.success) {
        this.clearUserCache();
        await this.fetchQuestionBankCoverage();
        await this.fetchStats();
        await this.fetchBookmarks();
        await this.fetchMistakes();
        this.closeWorkspaceModal();
        this.showToast("Your workspace progress has been cleanly reset.", 'success');
      } else {
        this.showToast(data.error || "Failed to reset workspace", 'error');
      }
    } catch (err) {
      console.error("Error resetting workspace:", err);
      this.showToast("Network error resetting workspace", 'error');
    }
  },

  // =========================================================================
  // Lifecycle & Initialization
  // =========================================================================

  async init() {
    this.initTheme();
    this.initKeyboardShortcuts();
    this.updateWorkspaceUI();
    await this.switchSet('A', false);
    await this.renderChapterSelectionGrid();
    await this.fetchQuestionBankCoverage();
    await this.fetchStats();
    await this.fetchBookmarks();
    await this.loadResearchLogs();
  },

  // Keyboard Shortcuts for Rapid Exam Navigation
  initKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
      if (this.mockExam.active && this.activeTab === 'mock') {
        if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;
        const key = e.key.toUpperCase();
        if (['A', '1'].includes(key)) {
          this.selectMockOption('A');
        } else if (['B', '2'].includes(key)) {
          this.selectMockOption('B');
        } else if (['C', '3'].includes(key)) {
          this.selectMockOption('C');
        } else if (['D', '4'].includes(key)) {
          this.selectMockOption('D');
        } else if (key === 'ENTER') {
          this.saveAndNext();
        } else if (key === 'ARROWLEFT') {
          this.prevQuestion();
        }
      } else if (this.practiceState.active && this.activeTab === 'practice') {
        if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;
        const key = e.key.toUpperCase();
        if (['A', '1'].includes(key)) {
          this.selectPracticeOption('A');
        } else if (['B', '2'].includes(key)) {
          this.selectPracticeOption('B');
        } else if (['C', '3'].includes(key)) {
          this.selectPracticeOption('C');
        } else if (['D', '4'].includes(key)) {
          this.selectPracticeOption('D');
        } else if (key === 'ENTER') {
          this.nextPracticeQuestion();
        } else if (key === 'ARROWLEFT') {
          this.prevPracticeQuestion();
        }
      }
    });
  },

  // Theme Management (Default: Light luxury brand aesthetic)
  initTheme() {
    const savedTheme = localStorage.getItem('spom_theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    const icon = document.getElementById('theme-icon');
    if (icon) {
      icon.textContent = savedTheme === 'dark' ? '🌙' : '☀️';
    }
  },

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('spom_theme', next);
    const icon = document.getElementById('theme-icon');
    if (icon) {
      icon.textContent = next === 'dark' ? '🌙' : '☀️';
    }
  },

  // Switch Active Module: Set A vs Set B
  async switchSet(setName, showToastMessage = true) {
    this.currentSet = setName.toUpperCase();

    const btnA = document.getElementById('set-a-btn');
    const btnB = document.getElementById('set-b-btn');

    if (btnA && btnB) {
      btnA.classList.toggle('active', this.currentSet === 'A');
      btnB.classList.toggle('active', this.currentSet === 'B');
    }

    const heroTitle = document.getElementById('hero-set-title');
    if (heroTitle) {
      heroTitle.textContent = this.currentSet === 'A'
        ? "Set A · Corporate and Economic Laws"
        : "Set B · Strategic Cost & Performance Mgmt";
    }

    const weightageBadge = document.getElementById('stat-weightage-badge');
    if (weightageBadge) {
      weightageBadge.textContent = this.currentSet === 'A'
        ? "Part I: 70M | Part II: 30M"
        : "Part I: 50M | Part II: 50M";
    }

    const splitBadge = document.getElementById('section-split-badge');
    if (splitBadge) {
      splitBadge.textContent = this.currentSet === 'A'
        ? "Part I: 70 Marks | Part II: 30 Marks"
        : "Part I: 50 Marks | Part II: 50 Marks";
    }

    if (showToastMessage) {
      this.showToast(`Switched to Set ${this.currentSet}`, 'info');
    }

    this.selectedChapters = [];
    await this.fetchChapters(this.currentSet);
    await this.fetchIntelligenceDashboard();
    await this.fetchQuestionBankCoverage();
    this.renderHomeChapters();
    this.renderChapterSelectionGrid();
    this.updateChapterDropdowns();
    this.updateChapterDropdownForForm();

    if (this.activeTab === 'handbook') {
      this.loadHandbookContent();
    } else if (this.activeTab === 'mistakes') {
      this.filterMistakes(this.currentMistakeFilter);
    } else if (this.activeTab === 'studio') {
      this.loadQBQuestions();
    } else if (this.activeTab === 'practice') {
      this.renderCoverageHub();
    }
  },

  // Tab View Routing
  showTab(tabName) {
    if (this.mockExam.active && this.activeTab === 'mock' && tabName !== 'mock') {
      if (!confirm("Your mock test is currently active! Do you wish to leave the examination screen? Your timer continues.")) {
        return;
      }
    }

    this.activeTab = tabName;

    // Update Top Navigation Buttons
    const navItems = ['home', 'handbook', 'practice', 'mistakes', 'studio'];
    navItems.forEach(item => {
      const btn = document.getElementById(`nav-${item}`);
      if (btn) btn.classList.toggle('active', item === tabName);
    });

    // Toggle Pane Displays
    const allPanes = document.querySelectorAll('.tab-pane');
    allPanes.forEach(pane => pane.classList.remove('active'));

    const activePane = document.getElementById(`tab-${tabName}`);
    if (activePane) activePane.classList.add('active');

    // Tab-Specific Data Refresh
    if (tabName === 'home') {
      this.fetchStats();
      this.fetchIntelligenceDashboard();
    } else if (tabName === 'handbook') {
      this.loadHandbookContent();
    } else if (tabName === 'mistakes') {
      this.filterMistakes(this.currentMistakeFilter);
    } else if (tabName === 'studio') {
      this.loadQBQuestions();
    } else if (tabName === 'practice') {
      this.fetchQuestionBankCoverage();
      this.renderChapterSelectionGrid();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  // =========================================================================
  // API Fetchers & Data Synchronization
  // =========================================================================

  async fetchStats() {
    const cached = this.getCache('stats');
    if (cached) {
      this.renderStatsData(cached);
    }
    try {
      const res = await this.apiFetch('/api/stats');
      const data = await res.json();
      if (data.success && data.data) {
        this.renderStatsData(data.data);
        this.setCache('stats', data.data);
      }
    } catch (err) {
      console.error("Error fetching stats:", err);
    }
  },

  renderStatsData(s) {
    const totalQEl = document.getElementById('stat-total-q');
    const passRateEl = document.getElementById('stat-pass-rate');
    const mistakesNav = document.getElementById('nav-mistakes-count');
    const recallsEl = document.getElementById('stat-offline-recalls');
    const highPriorityEl = document.getElementById('stat-high-priority-topics');

    if (totalQEl) totalQEl.textContent = s.total_mcqs || 0;
    if (passRateEl) passRateEl.textContent = `${s.pass_rate || 0}%`;
    if (mistakesNav) mistakesNav.textContent = s.unmastered_mistakes || 0;
    if (recallsEl) recallsEl.textContent = `${s.total_student_recalls || 148}+ Recalls`;
    if (highPriorityEl) highPriorityEl.textContent = `${s.high_priority_topics_count || 18} Topics`;
  },

  async fetchChapters(setName) {
    const cached = this.getCache(`chapters_${setName}`);
    if (cached) {
      this.chapters = cached;
    }
    try {
      const res = await this.apiFetch(`/api/chapters?set=${setName}`);
      const data = await res.json();
      if (data.success) {
        this.chapters = data.data;
        this.setCache(`chapters_${setName}`, data.data);
      }
    } catch (err) {
      console.error("Error fetching chapters:", err);
    }
  },

  async fetchBookmarks() {
    const cached = this.getCache('bookmarks');
    if (cached) {
      this.bookmarkedList = cached;
    }
    try {
      const res = await this.apiFetch('/api/bookmarks');
      const data = await res.json();
      if (data.success) {
        this.bookmarkedList = data.data;
        this.setCache('bookmarks', data.data);
      }
    } catch (err) {
      console.error("Error fetching bookmarks:", err);
    }
  },

  // =========================================================================
  // Dashboard & Study Priorities
  // =========================================================================

  async fetchIntelligenceDashboard() {
    try {
      const res = await this.apiFetch(`/api/intelligence/dashboard?set=${this.currentSet}`);
      const data = await res.json();
      if (data.success) {
        // Syllabus Metadata Banner
        if (data.syllabus) {
          const titleEl = document.getElementById('syllabus-scheme-title');
          const notesEl = document.getElementById('syllabus-scheme-notes');
          if (titleEl) titleEl.textContent = `${data.syllabus.scheme_name} (${data.syllabus.applicable_attempt})`;
          if (notesEl) notesEl.textContent = data.syllabus.law_applicable_notes;
        }

        // Render "What Should I Study Today?" recommendations
        const recs = data.study_today.recommended_topics || [];
        const weakChaps = data.study_today.weak_chapters || [];
        const container = document.getElementById('study-today-items-container');

        if (!container) return;

        if (recs.length === 0 && weakChaps.length === 0) {
          container.innerHTML = `
            <div style="background: var(--bg-surface); padding: 1.5rem; border-radius: var(--radius-md); text-align: center; color: var(--text-muted); font-size: 0.9rem; border: 1px solid var(--border-subtle);">
              All high-priority topics for Set ${this.currentSet} have been marked revised. Take a 100M Mock test to evaluate overall exam readiness.
            </div>
          `;
          return;
        }

        let html = '';

        // Weak chapters notification if user has errors logged
        if (weakChaps.length > 0) {
          html += `
            <div style="background: var(--danger-bg); border: 1px solid rgba(158, 67, 67, 0.2); border-radius: var(--radius-md); padding: 0.85rem 1.25rem; margin-bottom: 0.85rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
              <span style="font-size: 0.86rem; color: var(--danger);">
                <strong>Weak Chapters Target:</strong> ${weakChaps.map(c => `${c.chapter_code} (${c.mistake_count} errors)`).join(', ')}.
              </span>
              <button class="btn btn-secondary btn-sm" onclick="app.startPracticeSession('weak_area')">Drill Mistakes →</button>
            </div>
          `;
        }

        // High Priority Recommended Topics
        recs.forEach(t => {
          html += `
            <div class="study-today-item">
              <div>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem; flex-wrap: wrap;">
                  <span class="badge-priority very-high">Priority ${t.priority_score}/100</span>
                  <span class="badge primary">${t.chapter_code}</span>
                  <strong style="font-size: 0.92rem; color: var(--text-main);">${t.name}</strong>
                </div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">
                  ${t.subtopic ? `<span>${t.subtopic} · </span>` : ''}
                  <span>Recalls: <strong>${t.student_reports_count}</strong></span> · 
                  <span>Faculty Recs: <strong>${t.faculty_recs_count}</strong></span>
                </div>
              </div>
              <button class="btn btn-primary btn-sm" onclick="app.startPracticeOnTopic('${t.chapter_code}')">
                Practice →
              </button>
            </div>
          `;
        });

        container.innerHTML = html;
      }
    } catch (err) {
      console.error("Error fetching intelligence dashboard:", err);
    }
  },

  renderHomeChapters() {
    const container = document.getElementById('chapters-weightage-container');
    if (!container) return;

    if (!this.chapters || this.chapters.length === 0) {
      container.innerHTML = `<div style="padding: 2rem; text-align: center; color: var(--text-muted); grid-column: 1 / -1;">Loading official chapter blueprints...</div>`;
      return;
    }

    container.innerHTML = this.chapters.map(ch => {
      const tip = (ch.youtube_review_tips || '').replace(/🔥|⚡|⚠️|💡/g, '').trim();
      return `
        <div style="background: var(--bg-surface); padding: 1.25rem 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.35rem;">
              <h4 style="font-size: 1rem; font-weight: 600; color: var(--text-main);">${ch.name}</h4>
              <span class="badge" style="font-weight: 600; margin-left: 0.5rem;">${ch.weightage}</span>
            </div>
            <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-dim); margin-bottom: 0.6rem;">${ch.section_group}</div>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 0.75rem;">${ch.description || ''}</p>
          </div>
          ${tip ? `
            <div style="background: var(--bg-elevated); padding: 0.65rem 0.85rem; border-radius: var(--radius-sm); font-size: 0.82rem; color: var(--text-muted); border-left: 2px solid var(--accent-gold); margin-top: 0.5rem;">
              <span>Key Focus: ${tip}</span>
            </div>
          ` : ''}
        </div>
      `;
    }).join('');
  },

  updateChapterDropdowns() {
    const handbookSelect = document.getElementById('handbook-chapter-select');

    if (handbookSelect) {
      const optionsHtml = this.chapters.map(ch => `
        <option value="${ch.code}">[${ch.weightage}] ${ch.name}</option>
      `).join('');
      handbookSelect.innerHTML = optionsHtml;
      if (!this.currentHandbookChapter && this.chapters.length > 0) {
        this.currentHandbookChapter = this.chapters[0].code;
      }
    }
  },

  updateChapterDropdownForForm() {
    const formSelect = document.getElementById('new-mcq-chapter');
    if (formSelect) {
      formSelect.innerHTML = this.chapters.map(ch => `
        <option value="${ch.code}">${ch.code} - ${ch.name}</option>
      `).join('');
    }
  },

  // =========================================================================
  // Quick Revision Handbook & Integrated Priority Intelligence
  // =========================================================================

  switchHandbookCategory(category) {
    this.currentHandbookCategory = category;

    ['summary', 'limits', 'confused', 'traps', 'intelligence'].forEach(cat => {
      const btn = document.getElementById(`hb-tab-${cat}`);
      if (btn) btn.classList.toggle('active', cat === category);
    });

    const chapterSelectBox = document.getElementById('handbook-chapter-select')?.parentElement;
    if (chapterSelectBox) {
      chapterSelectBox.style.display = (category === 'intelligence') ? 'none' : 'flex';
    }

    this.loadHandbookContent();
  },

  async loadHandbookContent() {
    if (this.currentHandbookCategory === 'intelligence') {
      await this.renderHandbookIntelligenceTopics();
      return;
    }

    const chapterSelect = document.getElementById('handbook-chapter-select');
    const chapterCode = chapterSelect ? chapterSelect.value : (this.currentHandbookChapter || (this.chapters[0] ? this.chapters[0].code : 'A_DIR'));

    const container = document.getElementById('handbook-content-renderer');
    if (!container) return;

    try {
      const res = await this.apiFetch(`/api/handbook?set=${this.currentSet}&chapter=${chapterCode}`);
      const data = await res.json();

      if (!data.success || !data.data) {
        container.innerHTML = `<div class="card" style="text-align: center; color: var(--text-muted); padding: 3rem;">No handbook notes available for this chapter yet.</div>`;
        return;
      }

      const c = data.data.content;
      let renderedHtml = '';

      if (this.currentHandbookCategory === 'summary') {
        if (c.cheat_sheet) {
          renderedHtml += `
            <div class="card" style="margin-bottom: 1.5rem;">
              <h3 class="card-title" style="margin-bottom: 0.75rem;">Fast-Track Revision Blueprint</h3>
              <p style="font-size: 0.95rem; line-height: 1.7; color: var(--text-main);">${c.cheat_sheet}</p>
            </div>
          `;
        }
        if (c.core_provisions) {
          renderedHtml += `
            <div class="card">
              <h3 class="card-title" style="margin-bottom: 1rem;">Core Statutory / Standard Provisions</h3>
              <div style="display: grid; gap: 0.85rem;">
                ${c.core_provisions.map(p => `
                  <div style="padding: 0.85rem 1rem; background: var(--bg-elevated); border-radius: var(--radius-sm); border-left: 3px solid var(--accent-gold);">
                    <div style="font-weight: 600; font-size: 0.92rem; color: var(--text-main); margin-bottom: 0.25rem;">${p.title}</div>
                    <div style="font-size: 0.86rem; color: var(--text-muted); line-height: 1.6;">${p.provision}</div>
                  </div>
                `).join('')}
              </div>
            </div>
          `;
        }
      } else if (this.currentHandbookCategory === 'limits') {
        if (c.limits_table) {
          renderedHtml += `
            <table class="handbook-table">
              <thead>
                <tr>
                  <th>Statutory Subject / Standard Requirement</th>
                  <th>Legal Limit / Threshold / Ratio</th>
                  <th>Mandatory Benchmark</th>
                </tr>
              </thead>
              <tbody>
                ${c.limits_table.map(row => `
                  <tr>
                    <td><strong>${row.item}</strong></td>
                    <td style="color: var(--accent-gold); font-weight: 600;">${row.limit}</td>
                    <td>${row.context}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          `;
        } else if (c.formulas) {
          renderedHtml += `
            <div class="grid-2">
              ${c.formulas.map(f => `
                <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                  <h4 style="color: var(--accent-gold); margin-bottom: 0.35rem; font-size: 0.95rem;">${f.name}</h4>
                  <p style="font-size: 0.88rem; font-family: var(--font-mono); background: var(--bg-elevated); padding: 0.6rem; border-radius: 4px; color: var(--text-main);">
                    ${f.formula}
                  </p>
                </div>
              `).join('')}
            </div>
          `;
        }
      } else if (this.currentHandbookCategory === 'confused') {
        if (c.comparisons) {
          renderedHtml += `
            <table class="handbook-table">
              <thead>
                <tr>
                  <th>Concept A</th>
                  <th>Concept B</th>
                  <th>Crucial Legal / Costing Distinction</th>
                </tr>
              </thead>
              <tbody>
                ${c.comparisons.map(row => `
                  <tr>
                    <td style="font-weight: 600;">${row.concept_a}</td>
                    <td style="font-weight: 600;">${row.concept_b}</td>
                    <td>${row.difference}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          `;
        } else if (c.building_blocks) {
          renderedHtml += `
            <div class="grid-3">
              ${c.building_blocks.map(b => `
                <div class="card">
                  <h4 style="margin-bottom: 0.4rem; font-size: 0.95rem;">${b.block}</h4>
                  <p style="font-size: 0.85rem; line-height: 1.6; color: var(--text-muted);">${b.components}</p>
                </div>
              `).join('')}
            </div>
          `;
        }
      } else if (this.currentHandbookCategory === 'traps') {
        if (c.traps) {
          renderedHtml += c.traps.map(trap => `
            <div class="exam-trap-box" style="margin-bottom: 0.85rem; font-size: 0.9rem;">
              <span>${trap.replace(/⚠️/g, '').trim()}</span>
            </div>
          `).join('');
        }
      }

      container.innerHTML = renderedHtml || `<div class="card" style="text-align: center; color: var(--text-muted); padding: 2rem;">No data entries found for this category.</div>`;
    } catch (err) {
      console.error("Error loading handbook content:", err);
      container.innerHTML = `<div class="card" style="text-align: center; color: var(--danger); padding: 2rem;">Failed to load handbook content.</div>`;
    }
  },

  async renderHandbookIntelligenceTopics() {
    const container = document.getElementById('handbook-content-renderer');
    if (!container) return;

    try {
      const res = await this.apiFetch(`/api/intelligence/topics?set=${this.currentSet}`);
      const data = await res.json();

      if (!data.success || data.data.length === 0) {
        container.innerHTML = `<div class="card" style="text-align: center; color: var(--text-muted); padding: 3rem;">No priority records found.</div>`;
        return;
      }

      container.innerHTML = data.data.map(t => {
        let pClass = 'low';
        if (t.priority_score >= 85) pClass = 'very-high';
        else if (t.priority_score >= 70) pClass = 'high';
        else if (t.priority_score >= 50) pClass = 'medium';

        return `
          <div class="card" style="margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; flex-wrap: wrap; gap: 0.5rem;">
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span class="badge-priority ${pClass}">Score ${t.priority_score}/100</span>
                <span class="badge primary">${t.chapter_code}</span>
                <strong style="font-size: 1.05rem; color: var(--text-main);">${t.name}</strong>
              </div>
              <button class="btn btn-secondary btn-sm" onclick="app.startPracticeOnTopic('${t.chapter_code}')">
                Practice MCQs →
              </button>
            </div>

            ${t.subtopic ? `<div style="font-size: 0.85rem; color: var(--accent-gold); font-weight: 600; margin-bottom: 0.5rem;">Statutory Reference / Framework: ${t.subtopic}</div>` : ''}
            <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0.75rem; line-height: 1.6;">${t.description || ''}</p>

            <div style="display: flex; gap: 1rem; font-size: 0.8rem; color: var(--text-muted); border-top: 1px solid var(--border-subtle); padding-top: 0.6rem; flex-wrap: wrap;">
              <span>ICAI Base Weightage: <strong>${t.icai_score}/30</strong></span> · 
              <span>Student Offline Recalls: <strong>${t.student_recall_score}/25 (${t.student_reports_count} reports)</strong></span> · 
              <span>Faculty Recommendations: <strong>${t.faculty_score}/20</strong></span> · 
              <span>Case Rigor: <strong>${t.case_score}/15</strong></span> · 
              <span>Trap Density: <strong>${t.trap_score}/10</strong></span>
            </div>
          </div>
        `;
      }).join('');
    } catch (err) {
      console.error(err);
      container.innerHTML = `<div class="card" style="text-align: center; color: var(--danger); padding: 2rem;">Failed to load priority matrix.</div>`;
    }
  },

  startPracticeOnTopic(chapterCode) {
    this.showTab('practice');
    this.startPracticeSession('chapter', 10, chapterCode);
  },

  // =========================================================================
  // Chapter & Multi-Chapter Testing Studio Methods
  // =========================================================================

  async renderChapterSelectionGrid() {
    const grid = document.getElementById('chapter-select-grid');
    if (!grid) return;

    if (!this.chapters || this.chapters.length === 0) {
      await this.fetchChapters(this.currentSet);
    }

    if (!this.chapters || this.chapters.length === 0) {
      grid.innerHTML = `<div style="grid-column: 1 / -1; padding: 2rem; text-align: center; color: var(--text-muted);">No chapters available for Set ${this.currentSet}.</div>`;
      return;
    }

    grid.innerHTML = this.chapters.map(ch => {
      const isChecked = this.selectedChapters.includes(ch.code);
      const mcqCount = ch.mcq_count || 0;
      return `
        <label class="chapter-select-card ${isChecked ? 'selected' : ''}" id="card-chap-${ch.code}" for="chk-chap-${ch.code}">
          <input type="checkbox" id="chk-chap-${ch.code}" value="${ch.code}" ${isChecked ? 'checked' : ''} onchange="app.onChapterSelectionChanged()" />
          <div class="chap-card-body">
            <div class="chap-card-top">
              <span class="chap-code">${ch.code}</span>
              <span class="chap-weight">${ch.weightage}</span>
            </div>
            <div class="chap-name">${ch.name}</div>
            <div class="chap-card-bottom">
              <span class="chap-sec">${ch.section_group || ''}</span>
              <span class="chap-mcq-count">${mcqCount} MCQs</span>
            </div>
          </div>
        </label>
      `;
    }).join('');

    this.updateChapterSelectionSummary();
  },

  onChapterSelectionChanged() {
    const checkboxes = document.querySelectorAll('#chapter-select-grid input[type="checkbox"]');
    const selected = [];
    checkboxes.forEach(cb => {
      const card = document.getElementById(`card-chap-${cb.value}`);
      if (cb.checked) {
        selected.push(cb.value);
        if (card) card.classList.add('selected');
      } else {
        if (card) card.classList.remove('selected');
      }
    });

    this.selectedChapters = selected;
    this.updateChapterSelectionSummary();
  },

  updateChapterSelectionSummary() {
    const label = document.getElementById('chapter-selection-count-label');
    if (!label) return;

    let totalMcqs = 0;
    this.chapters.forEach(ch => {
      if (this.selectedChapters.includes(ch.code)) {
        totalMcqs += (ch.mcq_count || 0);
      }
    });

    if (this.selectedChapters.length === 0) {
      label.textContent = "0 Chapters Selected (0 MCQs)";
      label.style.color = "var(--text-muted)";
    } else {
      label.textContent = `${this.selectedChapters.length} of ${this.chapters.length} Chapters Selected (${totalMcqs} MCQs)`;
      label.style.color = "var(--text-main)";
    }
  },

  selectAllChapters(select = true) {
    if (select) {
      this.selectedChapters = this.chapters.map(ch => ch.code);
    } else {
      this.selectedChapters = [];
    }
    const checkboxes = document.querySelectorAll('#chapter-select-grid input[type="checkbox"]');
    checkboxes.forEach(cb => {
      cb.checked = select;
      const card = document.getElementById(`card-chap-${cb.value}`);
      if (card) card.classList.toggle('selected', select);
    });
    this.updateChapterSelectionSummary();
  },

  selectSectionChapters(sectionPrefix) {
    const targetCodes = this.chapters
      .filter(ch => (ch.section_group || '').toLowerCase().includes(sectionPrefix.toLowerCase()))
      .map(ch => ch.code);

    this.selectedChapters = targetCodes;
    const checkboxes = document.querySelectorAll('#chapter-select-grid input[type="checkbox"]');
    checkboxes.forEach(cb => {
      const isTarget = targetCodes.includes(cb.value);
      cb.checked = isTarget;
      const card = document.getElementById(`card-chap-${cb.value}`);
      if (card) card.classList.toggle('selected', isTarget);
    });
    this.updateChapterSelectionSummary();
  },

  selectHighWeightageChapters() {
    const targetCodes = this.chapters
      .filter(ch => {
        const w = ch.weightage || '';
        const highTerms = ['14', '15', '16', '18', '20', '22'];
        return highTerms.some(t => w.includes(t));
      })
      .map(ch => ch.code);

    this.selectedChapters = targetCodes.length > 0 ? targetCodes : this.chapters.slice(0, 3).map(c => c.code);
    const checkboxes = document.querySelectorAll('#chapter-select-grid input[type="checkbox"]');
    checkboxes.forEach(cb => {
      const isTarget = this.selectedChapters.includes(cb.value);
      cb.checked = isTarget;
      const card = document.getElementById(`card-chap-${cb.value}`);
      if (card) card.classList.toggle('selected', isTarget);
    });
    this.updateChapterSelectionSummary();
  },

  openChapterPracticeModal() {
    const card = document.getElementById('chapter-selection-card');
    if (card) {
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      card.classList.add('pulse-highlight');
      setTimeout(() => card.classList.remove('pulse-highlight'), 2500);
      this.showToast("Choose your individual chapter or combination of chapters in the Studio below.", 'info');
    }
  },

  // =========================================================================
  // Question Bank Coverage & Mastery Hub
  // =========================================================================

  switchTestingSubtab(subtab) {
    this.coverageState.activeSubtab = subtab;
    const subtabs = ['coverage', 'chapters', 'presets'];
    subtabs.forEach(st => {
      const btn = document.getElementById(`btn-subtab-${st}`);
      if (btn) btn.classList.toggle('active', st === subtab);

      const pane = document.getElementById(`testing-view-${st}`);
      if (pane) pane.style.display = (st === subtab) ? 'block' : 'none';
    });

    if (subtab === 'coverage') {
      this.fetchQuestionBankCoverage();
    } else if (subtab === 'chapters') {
      this.renderChapterSelectionGrid();
    }
  },

  async fetchQuestionBankCoverage() {
    const cached = this.getCache(`coverage_${this.currentSet}`);
    if (cached) {
      this.coverageState.data = cached;
      this.renderCoverageHub();
    }
    try {
      const res = await this.apiFetch(`/api/question-bank-coverage?set=${this.currentSet}`);
      const data = await res.json();
      if (data.success && data.data) {
        this.coverageState.data = data.data;
        this.setCache(`coverage_${this.currentSet}`, data.data);
        this.renderCoverageHub();
      }
    } catch (err) {
      console.error("Error fetching question bank coverage:", err);
    }
  },

  renderCoverageHub() {
    const d = this.coverageState.data;
    if (!d) return;

    const total = d.total_mcqs || 0;
    const attempted = d.attempted || 0;
    const never = d.never_attempted || 0;
    const wrong = d.wrong_many_times || 0;
    const correct = d.correct_many_times || 0;
    const covPct = d.coverage_pct || 0;

    // Header Badges & Headline Stats
    const setBadge = document.getElementById('coverage-set-badge');
    if (setBadge) {
      setBadge.textContent = this.currentSet === 'A' ? 'Set A · Corporate & Economic Laws' : 'Set B · Strategic Cost & Performance Mgmt';
    }

    const totalBankEl = document.getElementById('coverage-total-bank');
    if (totalBankEl) totalBankEl.textContent = `${total} High-Yield MCQs`;

    const pctHeadEl = document.getElementById('coverage-pct-headline');
    if (pctHeadEl) pctHeadEl.textContent = `${covPct}%`;

    const attStatEl = document.getElementById('coverage-attempted-stat');
    if (attStatEl) attStatEl.textContent = attempted;

    const totStatEl = document.getElementById('coverage-total-stat');
    if (totStatEl) totStatEl.textContent = total;

    // Progress Bar Segments
    const masteredPct = total > 0 ? ((correct / total) * 100) : 0;
    const wrongPct = total > 0 ? ((wrong / total) * 100) : 0;
    const unseenPct = total > 0 ? ((never / total) * 100) : 0;

    const barMastered = document.getElementById('cov-bar-mastered');
    if (barMastered) barMastered.style.width = `${masteredPct}%`;

    const barWrong = document.getElementById('cov-bar-wrong');
    if (barWrong) barWrong.style.width = `${wrongPct}%`;

    const barUnseen = document.getElementById('cov-bar-unseen');
    if (barUnseen) barUnseen.style.width = `${unseenPct}%`;

    // Legend
    const legMasteredCount = document.getElementById('leg-mastered-count');
    if (legMasteredCount) legMasteredCount.textContent = correct;
    const legMasteredPct = document.getElementById('leg-mastered-pct');
    if (legMasteredPct) legMasteredPct.textContent = `${masteredPct.toFixed(1)}%`;

    const legWrongCount = document.getElementById('leg-wrong-count');
    if (legWrongCount) legWrongCount.textContent = wrong;
    const legWrongPct = document.getElementById('leg-wrong-pct');
    if (legWrongPct) legWrongPct.textContent = `${wrongPct.toFixed(1)}%`;

    const legUnseenCount = document.getElementById('leg-unseen-count');
    if (legUnseenCount) legUnseenCount.textContent = never;
    const legUnseenPct = document.getElementById('leg-unseen-pct');
    if (legUnseenPct) legUnseenPct.textContent = `${unseenPct.toFixed(1)}%`;

    // 4 Cohort Cards Counts
    const cntNever = document.getElementById('cohort-count-never_attempted');
    if (cntNever) cntNever.textContent = never;
    const pctNever = document.getElementById('cohort-pct-never_attempted');
    if (pctNever) pctNever.textContent = `${unseenPct.toFixed(1)}%`;

    const cntWrong = document.getElementById('cohort-count-wrong_many_times');
    if (cntWrong) cntWrong.textContent = wrong;

    const cntCorrect = document.getElementById('cohort-count-correct_many_times');
    if (cntCorrect) cntCorrect.textContent = correct;

    const cntAtt = document.getElementById('cohort-count-attempted');
    if (cntAtt) cntAtt.textContent = attempted;
    const pctAtt = document.getElementById('cohort-pct-attempted');
    if (pctAtt) pctAtt.textContent = `${covPct}%`;

    // Update selected cohort state and launch panel
    this.selectCoverageCohort(this.coverageState.selectedCohort, false);

    // Render Chapter Breakdown Grid
    this.renderChapterCoverageList(d.chapters || []);
  },

  selectCoverageCohort(cohort, updateDropdown = true) {
    this.coverageState.selectedCohort = cohort;

    // Highlight the selected cohort card
    const cohortKeys = ['never_attempted', 'wrong_many_times', 'correct_many_times', 'attempted'];
    cohortKeys.forEach(k => {
      const card = document.getElementById(`card-cohort-${k}`);
      if (card) card.classList.toggle('selected', k === cohort);
    });

    const d = this.coverageState.data;
    if (!d) return;

    let title = "Never Attempted (Unseen Questions)";
    let subtitle = "Configure and launch a practice drill or timed mock on fresh, unseen questions to maximize bank coverage.";
    let totalInCohort = d.never_attempted || 0;

    if (cohort === 'wrong_many_times') {
      title = "Wrong Many Times (Needs Practice / Repeat Traps)";
      subtitle = "Drill into questions where you previously recorded errors or unresolved traps in My Mistakes Book.";
      totalInCohort = d.wrong_many_times || 0;
    } else if (cohort === 'correct_many_times') {
      title = "Correct Many Times (Mastered & Verified Accuracy)";
      subtitle = "Review questions you answered correctly to ensure long-term retention before exam day.";
      totalInCohort = d.correct_many_times || 0;
    } else if (cohort === 'attempted') {
      title = "All Questions Attempted (Cumulative Tested Pool)";
      subtitle = "Re-test the complete pool of questions you have encountered across all your CBT mocks and drills.";
      totalInCohort = d.attempted || 0;
    }

    const titleEl = document.getElementById('active-cohort-title');
    if (titleEl) titleEl.textContent = title;

    const subEl = document.getElementById('active-cohort-subtitle');
    if (subEl) subEl.textContent = subtitle;

    const availBadge = document.getElementById('active-cohort-available-count');
    if (availBadge) availBadge.textContent = `${totalInCohort} MCQs`;

    // Populate Chapter Filter dropdown for this cohort
    const chSelect = document.getElementById('cohort-chapter-select');
    if (chSelect && d.chapters) {
      const prevVal = this.coverageState.selectedChapter;
      chSelect.innerHTML = `<option value="all">All Chapters in Cohort (${totalInCohort} MCQs)</option>`;

      (d.chapters || []).forEach(ch => {
        let chCount = 0;
        if (cohort === 'never_attempted') chCount = ch.never_attempted || 0;
        else if (cohort === 'wrong_many_times') chCount = ch.wrong_many_times || 0;
        else if (cohort === 'correct_many_times') chCount = ch.correct_many_times || 0;
        else if (cohort === 'attempted') chCount = ch.attempted || 0;

        if (chCount > 0) {
          const opt = document.createElement('option');
          opt.value = ch.code;
          opt.textContent = `${ch.code}: ${ch.name} (${chCount} MCQs)`;
          chSelect.appendChild(opt);
        }
      });

      if (prevVal && chSelect.querySelector(`option[value="${prevVal}"]`)) {
        chSelect.value = prevVal;
      } else {
        chSelect.value = 'all';
        this.coverageState.selectedChapter = 'all';
      }
    }
  },

  onCohortChapterChange() {
    const chSelect = document.getElementById('cohort-chapter-select');
    if (chSelect) {
      this.coverageState.selectedChapter = chSelect.value;
    }
  },

  renderChapterCoverageList(chapters) {
    const listEl = document.getElementById('chapter-coverage-list');
    if (!listEl) return;

    if (!chapters || chapters.length === 0) {
      listEl.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted);">No chapter coverage data available.</div>`;
      return;
    }

    let html = `
      <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1.5fr; gap: 0.5rem; padding: 0.75rem 1rem; background: var(--bg-elevated); font-weight: 600; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-dim); border-bottom: 1px solid var(--border-subtle);">
        <div>Chapter</div>
        <div style="text-align: center;">Total</div>
        <div style="text-align: center;">Never</div>
        <div style="text-align: center;">Needs Work</div>
        <div style="text-align: center;">Mastered</div>
        <div style="text-align: right;">Coverage</div>
      </div>
    `;

    chapters.forEach(ch => {
      const tot = ch.total_mcqs || 0;
      const att = ch.attempted || 0;
      const nev = ch.never_attempted || 0;
      const wrg = ch.wrong_many_times || 0;
      const cor = ch.correct_many_times || 0;
      const pct = tot > 0 ? Math.round((att / tot) * 100) : 0;

      html += `
        <div class="chapter-coverage-row" style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1.5fr; gap: 0.5rem; align-items: center; padding: 0.75rem 1rem;">
          <div>
            <strong style="color: var(--text-main); font-size: 0.88rem;">${ch.code}</strong>
            <div style="font-size: 0.8rem; color: var(--text-muted); text-overflow: ellipsis; overflow: hidden; white-space: nowrap;" title="${ch.name}">${ch.name}</div>
          </div>
          <div style="text-align: center; font-weight: 600;">${tot}</div>
          <div style="text-align: center; color: var(--text-muted);">${nev}</div>
          <div style="text-align: center; color: var(--danger); font-weight: 600;">${wrg}</div>
          <div style="text-align: center; color: var(--success); font-weight: 600;">${cor}</div>
          <div style="text-align: right;">
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
              <span style="font-size: 0.78rem; font-weight: 600;">${pct}%</span>
              <div style="width: 50px; height: 6px; background: var(--bg-subtle); border-radius: 999px; overflow: hidden;">
                <div style="width: ${pct}%; height: 100%; background: ${pct >= 70 ? 'var(--success)' : pct >= 40 ? 'var(--accent-gold)' : 'var(--danger)'};"></div>
              </div>
            </div>
          </div>
        </div>
      `;
    });

    listEl.innerHTML = html;
  },

  toggleChapterCoverageDetails() {
    const container = document.getElementById('chapter-coverage-details-container');
    const btn = document.getElementById('btn-toggle-coverage-details');
    if (!container) return;

    const isHidden = container.style.display === 'none';
    container.style.display = isHidden ? 'block' : 'none';
    if (btn) {
      btn.textContent = isHidden ? 'Hide Detailed Chapter Grid ↑' : 'Show Detailed Chapter Grid ↓';
    }
  },

  launchCohortDrill() {
    const cohort = this.coverageState.selectedCohort || 'never_attempted';
    const chSelect = document.getElementById('cohort-chapter-select');
    const chapterCode = chSelect ? chSelect.value : 'all';

    const countSelect = document.getElementById('cohort-count-select');
    const count = countSelect ? parseInt(countSelect.value) : 10;

    this.startPracticeSession('mixed', count, chapterCode, cohort);
  },

  launchCohortMock() {
    const cohort = this.coverageState.selectedCohort || 'never_attempted';
    const chSelect = document.getElementById('cohort-chapter-select');
    const chapterCode = chSelect ? chSelect.value : 'all';

    const countSelect = document.getElementById('cohort-count-select');
    const count = countSelect ? parseInt(countSelect.value) : 20;

    this.startMockTest(this.currentSet, 'custom_chapters', chapterCode, count, cohort);
  },

  launchCustomChapterDrill() {
    if (!this.selectedChapters || this.selectedChapters.length === 0) {
      this.showToast("Please select at least one chapter from the Studio above to begin testing.", 'warning');
      const card = document.getElementById('chapter-selection-card');
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('pulse-highlight');
        setTimeout(() => card.classList.remove('pulse-highlight'), 2500);
      }
      return;
    }

    const countSelect = document.getElementById('custom-test-count');
    const count = countSelect ? parseInt(countSelect.value) : 10;
    const chaptersStr = this.selectedChapters.join(',');
    this.startPracticeSession('chapter', count, chaptersStr);
  },

  launchCustomChapterMock() {
    if (!this.selectedChapters || this.selectedChapters.length === 0) {
      this.showToast("Please select at least one chapter from the Studio above to begin testing.", 'warning');
      const card = document.getElementById('chapter-selection-card');
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('pulse-highlight');
        setTimeout(() => card.classList.remove('pulse-highlight'), 2500);
      }
      return;
    }

    const countSelect = document.getElementById('custom-test-count');
    const count = countSelect ? parseInt(countSelect.value) : 20;
    const chaptersStr = this.selectedChapters.join(',');
    this.startMockTest(this.currentSet, 'custom_chapters', chaptersStr, count);
  },

  // =========================================================================
  // Intelligent Practice Engine (10 Targeted Modes)
  // =========================================================================

  async startPracticeSession(mode, count = 10, chapterCode = null, cohort = null) {
    try {
      this.practiceState.active = true;
      this.practiceState.mode = mode;
      this.practiceState.chapterCode = chapterCode;
      this.practiceState.cohort = cohort;
      this.practiceState.count = count;
      this.practiceState.startTime = Date.now();
      this.practiceState.score = 0;
      this.practiceState.correctCount = 0;
      this.practiceState.incorrectCount = 0;
      this.showToast(`Loading practice questions...`, 'info');

      let url = `/api/practice/questions?set=${this.currentSet}&mode=${mode}&count=${count}&shuffle_options=true`;
      if (chapterCode && chapterCode !== 'all') url += `&chapters=${encodeURIComponent(chapterCode)}`;
      if (cohort) url += `&cohort=${encodeURIComponent(cohort)}`;

      const res = await this.apiFetch(url);
      const data = await res.json();

      if (!data.success || !data.questions || data.questions.length === 0) {
        this.showToast("No questions available for this practice selection", 'warning');
        return;
      }

      this.practiceState.questions = data.questions;
      this.practiceState.currentIndex = 0;
      this.practiceState.selectedOption = null;
      this.practiceState.isAnswerChecked = false;

      document.getElementById('practice-selector-view').style.display = 'none';
      document.getElementById('practice-quiz-view').style.display = 'block';

      const modeBadge = document.getElementById('practice-mode-badge');
      if (modeBadge) {
        let modeLabel = mode.toUpperCase();
        if (cohort) {
          const cohortNames = {
            never_attempted: 'Never Attempted (Unseen)',
            wrong_many_times: 'Wrong / Needs Practice',
            correct_many_times: 'Mastered / Consistent Correct',
            attempted: 'All Attempted Questions'
          };
          modeLabel = `Cohort: ${cohortNames[cohort] || cohort}`;
        } else if (chapterCode) {
          modeLabel = `Chapter Drill: ${chapterCode.replace(/,/g, ', ')}`;
        }
        modeBadge.textContent = `${modeLabel} · ${data.questions.length} Questions`;
      }

      this.renderPracticeQuestion();
    } catch (err) {
      console.error(err);
      this.showToast("Error loading practice questions", 'error');
    }
  },

  exitPracticeSession() {
    this.practiceState.active = false;
    document.getElementById('practice-quiz-view').style.display = 'none';
    document.getElementById('practice-selector-view').style.display = 'block';
    this.fetchQuestionBankCoverage();
  },

  renderPracticeQuestion() {
    const q = this.practiceState.questions[this.practiceState.currentIndex];
    if (!q) return;

    this.practiceState.isAnswerChecked = false;
    this.practiceState.selectedOption = null;

    // Reset feedback panel
    const feedbackPanel = document.getElementById('practice-feedback-panel');
    if (feedbackPanel) feedbackPanel.style.display = 'none';

    // Remove any mandatory alert styling on options container
    const optsContainer = document.getElementById('practice-options-container');
    if (optsContainer) optsContainer.classList.remove('options-mandatory-alert');

    const qCounter = document.getElementById('practice-q-counter');
    if (qCounter) qCounter.textContent = `Question ${this.practiceState.currentIndex + 1} of ${this.practiceState.questions.length}`;

    const qChapter = document.getElementById('practice-q-chapter');
    if (qChapter) qChapter.textContent = `${q.chapter_code} · ${q.topic || ''}`;

    const qSource = document.getElementById('practice-q-source');
    if (qSource) qSource.textContent = q.source_tag || 'ICAI BoS Module';

    const qMarks = document.getElementById('practice-q-marks');
    if (qMarks) qMarks.textContent = `[Marks: ${q.marks || 2}]`;

    // Case Study Scenario Banner
    const pCaseBox = document.getElementById('practice-case-box');
    const pCaseText = document.getElementById('practice-case-text');
    if (pCaseBox) {
      if (q.is_case_study && q.case_scenario) {
        pCaseBox.style.display = 'block';
        if (pCaseText) pCaseText.textContent = q.case_scenario;
      } else {
        pCaseBox.style.display = 'none';
      }
    }

    const qText = document.getElementById('practice-q-text');
    if (qText) qText.textContent = q.question;

    const starBtn = document.getElementById('practice-star-btn');
    if (starBtn) {
      const isBm = this.bookmarkedList.some(b => b.id === q.id);
      starBtn.classList.toggle('active', isBm);
    }

    // Render Options
    const opts = [
      { k: 'A', text: q.option_a },
      { k: 'B', text: q.option_b },
      { k: 'C', text: q.option_c },
      { k: 'D', text: q.option_d }
    ];

    if (optsContainer) {
      optsContainer.innerHTML = opts.map(o => `
        <div class="option-item" id="p-opt-${o.k}" onclick="app.selectPracticeOption('${o.k}')">
          <div class="option-letter">${o.k}</div>
          <div class="option-label">${o.text}</div>
        </div>
      `).join('');
    }

    const prevBtn = document.getElementById('btn-practice-prev');
    if (prevBtn) prevBtn.disabled = (this.practiceState.currentIndex === 0);

    const checkBtn = document.getElementById('btn-practice-check');
    if (checkBtn) {
      checkBtn.disabled = false;
      checkBtn.textContent = "Check Answer";
    }

    const nextBtn = document.getElementById('btn-practice-next');
    if (nextBtn) {
      const isLast = (this.practiceState.currentIndex === this.practiceState.questions.length - 1);
      nextBtn.textContent = isLast ? "Finish & Test Question →" : "Next Question →";
      nextBtn.className = "btn btn-primary btn-sm";
    }
  },

  selectPracticeOption(letter) {
    if (this.practiceState.isAnswerChecked) return;
    this.practiceState.selectedOption = letter;

    // Clear alert classes if user was prompted
    const optsContainer = document.getElementById('practice-options-container');
    if (optsContainer) optsContainer.classList.remove('options-mandatory-alert');

    document.querySelectorAll('#practice-options-container .option-item').forEach(el => {
      el.classList.remove('selected');
    });

    const target = document.getElementById(`p-opt-${letter}`);
    if (target) target.classList.add('selected');
  },

  async checkPracticeAnswer() {
    if (!this.practiceState.selectedOption) {
      this.showToast("Mandatory: Please select an option before checking", 'warning');
      const cont = document.getElementById('practice-options-container');
      if (cont) {
        cont.classList.remove('options-mandatory-alert');
        void cont.offsetWidth;
        cont.classList.add('options-mandatory-alert');
      }
      return false;
    }

    if (this.practiceState.isAnswerChecked) {
      return true; // Already tested
    }

    const q = this.practiceState.questions[this.practiceState.currentIndex];
    this.practiceState.isAnswerChecked = true;

    // Verify against shuffled correct key or canonical
    const correctKey = (q.shuffled_correct_key || q.correct_option || 'A').trim().toUpperCase();
    const isCorrect = (this.practiceState.selectedOption === correctKey);

    if (isCorrect) {
      this.practiceState.correctCount++;
      this.practiceState.score += (q.marks || 2);
    } else {
      this.practiceState.incorrectCount++;
    }

    // Selected text for DB mapping
    const optsMap = { A: q.option_a, B: q.option_b, C: q.option_c, D: q.option_d };
    const selectedText = optsMap[this.practiceState.selectedOption] || '';

    // Record attempt asynchronously into DB & Mistakes Book
    this.apiFetch('/api/record-practice-attempt', {
      method: 'POST',
      body: {
        mcq_id: q.id,
        is_correct: isCorrect,
        selected_text: selectedText
      }
    }).then(() => {
      this.fetchQuestionBankCoverage();
      this.fetchStats();
    }).catch(e => console.error("Error recording practice attempt:", e));

    // Highlight options in Review State
    document.querySelectorAll('#practice-options-container .option-item').forEach(el => {
      el.classList.add('review-neutral');
    });

    const correctEl = document.getElementById(`p-opt-${correctKey}`);
    if (correctEl) {
      correctEl.classList.remove('review-neutral');
      correctEl.classList.add('review-correct');
    }

    if (!isCorrect) {
      const pickedEl = document.getElementById(`p-opt-${this.practiceState.selectedOption}`);
      if (pickedEl) {
        pickedEl.classList.remove('review-neutral');
        pickedEl.classList.add('review-user-wrong');
      }
    }

    // Populate statutory feedback panel
    const feedbackPanel = document.getElementById('practice-feedback-panel');
    const resultPill = document.getElementById('practice-result-pill');

    if (isCorrect) {
      resultPill.className = 'badge success';
      resultPill.textContent = 'Correct (+2 Marks)';
    } else {
      resultPill.className = 'badge danger';
      resultPill.textContent = `Incorrect (Selected Option ${this.practiceState.selectedOption})`;
    }

    document.getElementById('practice-explanation-text').textContent = q.explanation || '';

    // Build Option-by-Option Breakdown
    const breakdownContainer = document.getElementById('practice-options-breakdown');
    const reasons = [
      { k: 'A', why: q.why_incorrect_a },
      { k: 'B', why: q.why_incorrect_b },
      { k: 'C', why: q.why_incorrect_c },
      { k: 'D', why: q.why_incorrect_d }
    ];

    let breakdownHtml = '';
    reasons.forEach(r => {
      if (r.k === correctKey) {
        breakdownHtml += `<div class="option-why-box correct-reason"><strong>Option ${r.k} [Correct]:</strong> Conforms to the statutory requirement / standard.</div>`;
      } else if (r.why) {
        breakdownHtml += `<div class="option-why-box incorrect-reason"><strong>Option ${r.k} [Incorrect]:</strong> ${r.why}</div>`;
      }
    });

    if (breakdownContainer) breakdownContainer.innerHTML = breakdownHtml;

    const secRefEl = document.getElementById('practice-section-ref');
    if (secRefEl) secRefEl.textContent = q.section_ref ? `Section / Standard: ${q.section_ref}` : '';

    const trapEl = document.getElementById('practice-exam-tip');
    if (trapEl) trapEl.innerHTML = `<span>Exam Trap: ${q.exam_tip || 'Remember this core rule.'}</span>`;

    if (feedbackPanel) feedbackPanel.style.display = 'block';

    const checkBtn = document.getElementById('btn-practice-check');
    if (checkBtn) {
      checkBtn.disabled = true;
      checkBtn.textContent = "Tested ✓";
    }

    // Update Next button to allow advancing
    const nextBtn = document.getElementById('btn-practice-next');
    if (nextBtn) {
      const isLast = (this.practiceState.currentIndex === this.practiceState.questions.length - 1);
      nextBtn.textContent = isLast ? "Finish Drill & View Results →" : "Continue to Next Question →";
      nextBtn.className = "btn btn-primary btn-sm";
    }

    return true;
  },

  async nextPracticeQuestion() {
    // 1. MANDATORY CHECK: Candidate MUST select an option
    if (!this.practiceState.selectedOption) {
      this.showToast("Mandatory: You must select an answer before proceeding to the next question.", 'warning');
      const cont = document.getElementById('practice-options-container');
      if (cont) {
        cont.classList.remove('options-mandatory-alert');
        void cont.offsetWidth; // Force CSS reflow to retrigger animation
        cont.classList.add('options-mandatory-alert');
      }
      return; // Block advancing!
    }

    // 2. MANDATORY CHECK: Candidate's answer MUST be tested before moving to next question
    if (!this.practiceState.isAnswerChecked) {
      await this.checkPracticeAnswer();
      const isCorrect = (this.practiceState.selectedOption === (this.practiceState.questions[this.practiceState.currentIndex].shuffled_correct_key || this.practiceState.questions[this.practiceState.currentIndex].correct_option));
      this.showToast(isCorrect ? "Correct (+2M)! Review rationale, then click Continue." : "Incorrect. Review statutory rationale below, then click Continue.", isCorrect ? 'success' : 'error');
      // Candidate must see evaluated rationale on this question before moving forward
      return;
    }

    // 3. Candidate's answer is evaluated and tested; now proceed to next question
    if (this.practiceState.currentIndex < this.practiceState.questions.length - 1) {
      this.practiceState.currentIndex++;
      this.renderPracticeQuestion();
      document.getElementById('practice-card')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      this.finishPracticeSession();
    }
  },

  prevPracticeQuestion() {
    if (this.practiceState.currentIndex > 0) {
      this.practiceState.currentIndex--;
      this.renderPracticeQuestion();
    }
  },

  finishPracticeSession() {
    const total = this.practiceState.questions.length;
    const correct = this.practiceState.correctCount;
    const incorrect = this.practiceState.incorrectCount;
    const score = this.practiceState.score;
    const maxMarks = total * 2;
    const pct = maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0;
    const timeSpentSec = Math.round((Date.now() - (this.practiceState.startTime || Date.now())) / 1000);
    const mins = Math.floor(timeSpentSec / 60);
    const secs = timeSpentSec % 60;

    const modal = document.getElementById('practice-complete-modal');
    if (modal) {
      const title = document.getElementById('practice-complete-title');
      const subtitle = document.getElementById('practice-complete-subtitle');
      const scoreEl = document.getElementById('practice-complete-score');
      const pctEl = document.getElementById('practice-complete-pct');
      const ratioEl = document.getElementById('practice-complete-ratio');
      const timeEl = document.getElementById('practice-complete-time');
      const notesEl = document.getElementById('practice-complete-notes');

      if (title) title.textContent = pct >= 50 ? "Drill Qualified (Pass Standard)" : "Drill Incomplete (Below 50%)";
      if (subtitle) subtitle.textContent = `Completed ${total} tested question(s) with mandatory evaluation.`;
      if (scoreEl) scoreEl.textContent = `${score} / ${maxMarks} M`;
      if (pctEl) {
        pctEl.textContent = `${pct}%`;
        pctEl.style.color = pct >= 50 ? 'var(--success)' : 'var(--danger)';
      }
      if (ratioEl) ratioEl.textContent = `${correct} / ${total}`;
      if (timeEl) timeEl.textContent = `Time: ${mins}m ${secs}s`;
      if (notesEl) {
        if (incorrect > 0) {
          notesEl.innerHTML = `${incorrect} incorrect question(s) have been automatically catalogued in <strong>My Mistakes Book</strong> for spaced revision.`;
        } else {
          notesEl.innerHTML = `Flawless score! 100% accuracy recorded across all questions in this drill.`;
        }
      }

      modal.classList.add('active');
    }

    this.fetchStats();
  },

  closePracticeCompleteModal() {
    const modal = document.getElementById('practice-complete-modal');
    if (modal) modal.classList.remove('active');
  },

  restartCurrentPractice() {
    this.closePracticeCompleteModal();
    this.startPracticeSession(this.practiceState.mode, this.practiceState.count, this.practiceState.chapterCode);
  },

  // =========================================================================
  // Mistakes Book & Spaced Revision Engine
  // =========================================================================

  filterMistakes(filterType) {
    this.currentMistakeFilter = filterType;

    ['all', 'unrevised', 'reviewed', 'mastered', 'starred'].forEach(f => {
      const btn = document.getElementById(`mb-filter-${f}`);
      if (btn) btn.classList.toggle('active', f === filterType);
    });

    const container = document.getElementById('mistakes-list-container');
    if (!container) return;

    if (filterType === 'starred') {
      if (this.bookmarkedList.length === 0) {
        container.innerHTML = `
          <div class="card" style="text-align: center; color: var(--text-muted); padding: 3rem;">
            <h3 style="margin-bottom: 0.5rem; font-family: var(--font-serif); font-size: 1.25rem;">No Starred Questions Yet</h3>
            <p>Click the ★ star icon on any question during Mock Tests or Practice Drills to save it here for rapid revision.</p>
          </div>
        `;
        return;
      }

      container.innerHTML = this.bookmarkedList.map((q, idx) => `
        <div class="review-question-card" style="border-left: 3px solid var(--accent-gold);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <span class="badge warning">★ STARRED</span>
              <span class="badge primary">${q.chapter_code} · ${q.topic || ''}</span>
              <span class="badge">${q.source_tag || 'ICAI BoS Module'}</span>
            </div>
            <button class="btn btn-secondary btn-sm" onclick="app.toggleBookmark(${q.id})">Remove Star</button>
          </div>

          <h4 style="font-size: 1rem; line-height: 1.6; margin-bottom: 1rem; font-weight: 600;">${idx + 1}. ${q.question}</h4>

          <div class="options-container" style="margin-bottom: 1rem;">
            ${[
              { k: 'A', text: q.option_a },
              { k: 'B', text: q.option_b },
              { k: 'C', text: q.option_c },
              { k: 'D', text: q.option_d }
            ].map(o => `
              <div class="option-item ${o.k === q.correct_option ? 'review-correct' : 'review-neutral'}">
                <div class="option-letter">${o.k}</div>
                <div class="option-label">${o.text}</div>
                ${o.k === q.correct_option ? '<span class="badge success" style="margin-left: auto;">Correct Option</span>' : ''}
              </div>
            `).join('')}
          </div>

          <div class="explanation-box" style="margin-top: 0.5rem;">
            <h6>Legal Authority & Explanation</h6>
            <p style="font-size: 0.9rem; line-height: 1.6; color: var(--text-main);">${q.explanation || ''}</p>
            ${q.section_ref ? `<div style="font-size: 0.82rem; color: var(--accent-gold); margin-top: 0.35rem;">Section / Standard: ${q.section_ref}</div>` : ''}
          </div>
        </div>
      `).join('');
      return;
    }

    // Load actual mistakes from backend
    this.loadMistakesFromBackend();
  },

  async loadMistakesFromBackend() {
    try {
      let url = `/api/mistakes?set=${this.currentSet}`;
      if (this.currentMistakeFilter !== 'all') {
        // capitalize filter for backend: unrevised -> Unrevised
        const capStatus = this.currentMistakeFilter.charAt(0).toUpperCase() + this.currentMistakeFilter.slice(1);
        url += `&status=${encodeURIComponent(capStatus)}`;
      }

      const res = await this.apiFetch(url);
      const data = await res.json();
      if (data.success) {
        this.mistakesList = data.data;
        this.renderMistakesBook(this.mistakesList);
      }
    } catch (err) {
      console.error("Error loading mistakes:", err);
    }
  },

  renderMistakesBook(mistakes) {
    const container = document.getElementById('mistakes-list-container');
    if (!container) return;

    if (!mistakes || mistakes.length === 0) {
      container.innerHTML = `
        <div class="card" style="text-align: center; color: var(--text-muted); padding: 3rem;">
          <h3 style="margin-bottom: 0.5rem; font-family: var(--font-serif); font-size: 1.25rem;">No Mistakes in this Filter</h3>
          <p>Any incorrect answers from Mocks or Practice Drills are automatically logged here for spaced revision.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = mistakes.map(m => {
      const statusClass = m.revision_status === 'Mastered' ? 'mastered' : (m.revision_status === 'Reviewed' ? 'reviewed' : '');
      const statusBadge = m.revision_status === 'Mastered' ? 'success' : (m.revision_status === 'Reviewed' ? 'warning' : 'danger');

      return `
        <div class="mistake-card ${statusClass}">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
            <div>
              <span class="badge ${statusBadge}">${(m.revision_status || 'UNREVISED').toUpperCase()}</span>
              <span class="badge primary">${m.chapter_code} · ${m.topic || ''}</span>
              <span class="mistake-count-badge">Tested: ${m.incorrect_count || 1} error(s)</span>
            </div>
            <div style="display: flex; gap: 0.35rem;">
              <button class="btn btn-secondary btn-sm" onclick="app.updateMistakeStatus(${m.id}, 'Reviewed')">Mark Reviewed</button>
              <button class="btn btn-secondary btn-sm" onclick="app.updateMistakeStatus(${m.id}, 'Mastered')">Mark Mastered ✓</button>
            </div>
          </div>

          <h4 style="font-size: 1rem; line-height: 1.6; margin-bottom: 0.75rem; font-weight: 600;">${m.question}</h4>

          <div style="display: flex; gap: 0.75rem; font-size: 0.85rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
            <div style="background: var(--danger-bg); padding: 0.35rem 0.65rem; border-radius: var(--radius-sm); border: 1px solid rgba(158, 67, 67, 0.2);">
              Your Last Pick: <strong style="color: var(--danger);">Option ${m.last_selected_option || 'N/A'}</strong>
            </div>
            <div style="background: var(--success-bg); padding: 0.35rem 0.65rem; border-radius: var(--radius-sm); border: 1px solid rgba(59, 107, 80, 0.2);">
              Correct Answer: <strong style="color: var(--success);">Option ${m.correct_option}</strong>
            </div>
          </div>

          <div class="explanation-box" style="margin-top: 0.5rem;">
            <h6>Legal Authority & Explanation</h6>
            <p style="font-size: 0.9rem; line-height: 1.6; color: var(--text-main);">${m.explanation || ''}</p>
            ${m.section_ref ? `<div style="font-size: 0.85rem; color: var(--accent-gold); font-weight: 600; margin-top: 0.25rem;">Section / Standard: ${m.section_ref}</div>` : ''}
            ${m.exam_tip ? `<div class="exam-trap-box" style="margin-top: 0.5rem;"><span>Trap Alert: ${m.exam_tip}</span></div>` : ''}
          </div>
        </div>
      `;
    }).join('');
  },

  async updateMistakeStatus(mistakeId, status) {
    try {
      const res = await this.apiFetch('/api/mistakes/status', {
        method: 'POST',
        body: { mistake_id: mistakeId, status }
      });
      const data = await res.json();
      if (data.success) {
        this.showToast(`Updated to ${status}`, 'success');
        this.filterMistakes(this.currentMistakeFilter);
        this.fetchStats();
      }
    } catch (err) {
      console.error(err);
      this.showToast("Failed to update status", 'error');
    }
  },

  // =========================================================================
  // CBT Mock Test Simulator (TCS iON Emulation)
  // =========================================================================

  promptMockStart() {
    if (this.mockExam.active) {
      this.showTab('mock');
    } else {
      this.startMockTest(this.currentSet, 'full_mock_50');
    }
  },

  async startMockTest(setName, mode = 'full_mock_50', chapters = null, count = 50, cohort = null) {
    try {
      this.currentMockMode = mode;
      this.showToast(`Assembling exam for Set ${setName}...`, 'info');

      let url = `/api/mock-test?set=${setName}&mode=${mode}&shuffle_options=true`;
      if (chapters && chapters !== 'all') url += `&chapters=${encodeURIComponent(chapters)}&count=${count}`;
      if (cohort) url += `&cohort=${encodeURIComponent(cohort)}&count=${count}`;

      const res = await this.apiFetch(url);
      const data = await res.json();

      if (!data.success) {
        this.showToast(data.error || "Failed to load mock test", 'error');
        return;
      }

      this.mockExam.active = true;
      this.mockExam.questions = data.questions;
      this.mockExam.currentIndex = 0;
      this.mockExam.userResponses = {}; // q_id -> letter
      this.mockExam.correctKeysMap = {};
      this.mockExam.totalQuestions = data.total_questions;
      this.mockExam.maxMarks = data.total_marks;
      this.mockExam.timeRemaining = data.duration_minutes * 60;
      this.mockExam.startTime = Date.now();

      // Store server shuffled correct keys
      this.mockExam.questions.forEach(q => {
        this.mockExam.correctKeysMap[q.id] = q.shuffled_correct_key;
      });

      // Initialize statuses
      this.mockExam.statuses = new Array(this.mockExam.questions.length).fill('not-visited');
      this.mockExam.statuses[0] = 'not-answered';

      // Update Section Tabs
      this.setupSectionTabs(setName);
      this.startTimer();
      this.showTab('mock');
      this.renderCurrentMockQuestion();
      this.renderQuestionPalette();
      this.updatePaletteSummary();
    } catch (err) {
      console.error(err);
      this.showToast("Failed to start CBT Mock", 'error');
    }
  },

  setupSectionTabs(setName) {
    const sec1Btn = document.getElementById('sec-tab-p1');
    const sec2Btn = document.getElementById('sec-tab-p2');

    if (setName === 'A') {
      if (sec1Btn) sec1Btn.innerHTML = `Part I: Corp Laws (<span id="sec-count-p1">35</span>)`;
      if (sec2Btn) sec2Btn.innerHTML = `Part II: Econ Laws (<span id="sec-count-p2">15</span>)`;
    } else {
      if (sec1Btn) sec1Btn.innerHTML = `Part I: Strategic Cost (<span id="sec-count-p1">25</span>)`;
      if (sec2Btn) sec2Btn.innerHTML = `Part II: Perf Mgmt (<span id="sec-count-p2">25</span>)`;
    }

    const badgeSet = document.getElementById('exam-badge-set');
    if (badgeSet) {
      badgeSet.textContent = setName === 'A'
        ? "SET A · CORPORATE & ECONOMIC LAWS (100M)"
        : "SET B · STRATEGIC COST & PERFORMANCE MGMT (100M)";
    }
  },

  filterMockSection(sec) {
    this.mockExam.currentSectionFilter = sec;

    ['all', 'Part I', 'Part II'].forEach(s => {
      const btnId = s === 'all' ? 'sec-tab-all' : (s === 'Part I' ? 'sec-tab-p1' : 'sec-tab-p2');
      const btn = document.getElementById(btnId);
      if (btn) btn.classList.toggle('active', s === sec);
    });

    this.renderQuestionPalette();

    // Auto navigate to first question in section if current question is outside
    const currentQ = this.mockExam.questions[this.mockExam.currentIndex];
    if (sec !== 'all' && currentQ && !currentQ.section_group.includes(sec)) {
      const idx = this.mockExam.questions.findIndex(q => q.section_group.includes(sec));
      if (idx !== -1) this.navigateToQuestion(idx);
    }
  },

  startTimer() {
    clearInterval(this.mockExam.timerInterval);
    const timerText = document.getElementById('timer-text');

    this.mockExam.timerInterval = setInterval(() => {
      if (this.mockExam.timeRemaining <= 0) {
        clearInterval(this.mockExam.timerInterval);
        this.showToast("Time expired. Submitting exam automatically...", 'warning');
        this.executeSubmitTest();
        return;
      }
      this.mockExam.timeRemaining--;

      const hrs = Math.floor(this.mockExam.timeRemaining / 3600);
      const mins = Math.floor((this.mockExam.timeRemaining % 3600) / 60);
      const secs = this.mockExam.timeRemaining % 60;

      const pad = (n) => String(n).padStart(2, '0');
      if (timerText) {
        timerText.textContent = hrs > 0
          ? `${pad(hrs)}:${pad(mins)}:${pad(secs)}`
          : `${pad(mins)}:${pad(secs)}`;
      }
    }, 1000);
  },

  renderCurrentMockQuestion() {
    const q = this.mockExam.questions[this.mockExam.currentIndex];
    if (!q) return;

    const currQNum = document.getElementById('curr-q-num');
    if (currQNum) currQNum.textContent = this.mockExam.currentIndex + 1;

    const totalQNum = document.getElementById('total-q-num');
    if (totalQNum) totalQNum.textContent = this.mockExam.questions.length;

    const currQMarks = document.getElementById('curr-q-marks');
    if (currQMarks) currQMarks.textContent = `[Marks: ${q.marks || 2} | Negative: 0]`;

    const currQChapter = document.getElementById('curr-q-chapter');
    if (currQChapter) currQChapter.textContent = `${q.section_group} · ${q.chapter_code}`;

    const currQSource = document.getElementById('curr-q-source');
    if (currQSource) currQSource.textContent = q.source_tag || 'ICAI BoS Module';

    // Case Study Scenario Banner
    const caseBox = document.getElementById('exam-case-box');
    const caseText = document.getElementById('exam-case-text');
    if (caseBox) {
      if (q.is_case_study && q.case_scenario) {
        caseBox.style.display = 'block';
        if (caseText) caseText.textContent = q.case_scenario;
      } else {
        caseBox.style.display = 'none';
      }
    }

    const qText = document.getElementById('curr-q-text');
    if (qText) qText.textContent = q.question;

    // Render Options
    const userSelected = this.mockExam.userResponses[q.id] || null;
    const opts = [
      { k: 'A', text: q.option_a },
      { k: 'B', text: q.option_b },
      { k: 'C', text: q.option_c },
      { k: 'D', text: q.option_d }
    ];

    const container = document.getElementById('curr-options-container');
    if (container) {
      container.innerHTML = opts.map(o => `
        <div class="option-item ${userSelected === o.k ? 'selected' : ''}" id="mock-opt-${o.k}" onclick="app.selectMockOption('${o.k}')">
          <div class="option-letter">${o.k}</div>
          <div class="option-label">${o.text}</div>
        </div>
      `).join('');
    }

    // Star icon state
    const starBtn = document.getElementById('curr-q-star-btn');
    if (starBtn) {
      const isBm = this.bookmarkedList.some(b => b.id === q.id);
      starBtn.classList.toggle('active', isBm);
    }

    const prevBtn = document.getElementById('btn-prev-q');
    if (prevBtn) prevBtn.disabled = this.mockExam.currentIndex === 0;

    this.updatePaletteActiveButton();
  },

  selectMockOption(letter) {
    const q = this.mockExam.questions[this.mockExam.currentIndex];
    this.mockExam.userResponses[q.id] = letter;

    document.querySelectorAll('#curr-options-container .option-item').forEach(el => {
      el.classList.remove('selected');
    });

    const target = document.getElementById(`mock-opt-${letter}`);
    if (target) target.classList.add('selected');
  },

  saveAndNext() {
    const q = this.mockExam.questions[this.mockExam.currentIndex];
    const ans = this.mockExam.userResponses[q.id];

    if (ans) {
      this.mockExam.statuses[this.mockExam.currentIndex] = 'answered';
    } else {
      if (this.mockExam.statuses[this.mockExam.currentIndex] !== 'marked-review') {
        this.mockExam.statuses[this.mockExam.currentIndex] = 'not-answered';
      }
    }

    this.advanceToNextQuestion();
  },

  markForReviewAndNext() {
    const q = this.mockExam.questions[this.mockExam.currentIndex];
    const ans = this.mockExam.userResponses[q.id];

    if (ans) {
      this.mockExam.statuses[this.mockExam.currentIndex] = 'answered-marked';
    } else {
      this.mockExam.statuses[this.mockExam.currentIndex] = 'marked-review';
    }

    this.advanceToNextQuestion();
  },

  clearCurrentResponse() {
    const q = this.mockExam.questions[this.mockExam.currentIndex];
    delete this.mockExam.userResponses[q.id];

    this.mockExam.statuses[this.mockExam.currentIndex] = 'not-answered';

    document.querySelectorAll('#curr-options-container .option-item').forEach(el => {
      el.classList.remove('selected');
    });

    this.renderQuestionPalette();
    this.updatePaletteSummary();
  },

  advanceToNextQuestion() {
    this.renderQuestionPalette();
    this.updatePaletteSummary();

    if (this.mockExam.currentIndex < this.mockExam.questions.length - 1) {
      this.mockExam.currentIndex++;
      if (this.mockExam.statuses[this.mockExam.currentIndex] === 'not-visited') {
        this.mockExam.statuses[this.mockExam.currentIndex] = 'not-answered';
      }
      this.renderCurrentMockQuestion();
    } else {
      this.showToast("Reached last question. Submit when ready.", 'info');
    }
  },

  prevQuestion() {
    if (this.mockExam.currentIndex > 0) {
      this.mockExam.currentIndex--;
      this.renderCurrentMockQuestion();
    }
  },

  navigateToQuestion(index) {
    if (index >= 0 && index < this.mockExam.questions.length) {
      this.mockExam.currentIndex = index;
      if (this.mockExam.statuses[index] === 'not-visited') {
        this.mockExam.statuses[index] = 'not-answered';
      }
      this.renderCurrentMockQuestion();
      this.renderQuestionPalette();
      this.updatePaletteSummary();
    }
  },

  renderQuestionPalette() {
    const grid = document.getElementById('palette-grid-buttons');
    if (!grid) return;

    const filter = this.mockExam.currentSectionFilter;

    grid.innerHTML = this.mockExam.questions.map((q, idx) => {
      if (filter !== 'all' && !q.section_group.includes(filter)) {
        return '';
      }

      const status = this.mockExam.statuses[idx] || 'not-visited';
      const isCurrent = idx === this.mockExam.currentIndex;

      return `
        <button class="palette-btn ${status} ${isCurrent ? 'current-active' : ''}" onclick="app.navigateToQuestion(${idx})">
          ${idx + 1}
        </button>
      `;
    }).join('');
  },

  updatePaletteActiveButton() {
    const allBtns = document.querySelectorAll('#palette-grid-buttons .palette-btn');
    allBtns.forEach((btn, idx) => {
      btn.classList.toggle('current-active', idx === this.mockExam.currentIndex);
    });
  },

  updatePaletteSummary() {
    const counts = {
      answered: 0,
      'not-answered': 0,
      'not-visited': 0,
      'marked-review': 0,
      'answered-marked': 0
    };

    this.mockExam.statuses.forEach(s => {
      if (counts[s] !== undefined) counts[s]++;
      else counts['not-visited']++;
    });

    const summaryBox = document.getElementById('palette-count-summary');
    if (summaryBox) {
      summaryBox.innerHTML = `
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; padding: 0.35rem 0;">
          <span style="color: var(--success);">Answered:</span>
          <strong>${counts.answered}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; padding: 0.35rem 0;">
          <span style="color: var(--danger);">Not Answered:</span>
          <strong>${counts['not-answered']}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; padding: 0.35rem 0;">
          <span style="color: var(--cbt-review);">Marked for Review:</span>
          <strong>${counts['marked-review']}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; padding: 0.35rem 0;">
          <span style="color: var(--text-muted);">Not Visited:</span>
          <strong>${counts['not-visited']}</strong>
        </div>
      `;
    }
  },

  confirmSubmitModal() {
    const total = this.mockExam.questions.length;
    let answered = 0;
    this.mockExam.statuses.forEach(s => {
      if (s === 'answered' || s === 'answered-marked') answered++;
    });
    const unattempted = total - answered;

    const totalEl = document.getElementById('modal-total-count');
    const ansEl = document.getElementById('modal-answered-count');
    const unansEl = document.getElementById('modal-unanswered-count');
    const revEl = document.getElementById('modal-review-count');

    if (totalEl) totalEl.textContent = total;
    if (ansEl) ansEl.textContent = answered;
    if (unansEl) unansEl.textContent = unattempted;
    if (revEl) {
      const reviewCount = this.mockExam.statuses.filter(s => s === 'marked-review' || s === 'answered-marked').length;
      revEl.textContent = reviewCount;
    }

    const modal = document.getElementById('submit-confirm-modal');
    if (modal) modal.classList.add('active');
  },

  closeSubmitModal() {
    const modal = document.getElementById('submit-confirm-modal');
    if (modal) modal.classList.remove('active');
  },

  async executeSubmitTest() {
    this.closeSubmitModal();
    clearInterval(this.mockExam.timerInterval);
    this.mockExam.active = false;

    const timeSpent = Math.max(1, Math.floor((Date.now() - this.mockExam.startTime) / 1000));

    // Send complete questions list with user selected keys and presented options
    const payload = {
      set_name: this.currentSet,
      mode: this.currentMockMode,
      time_taken_seconds: timeSpent,
      responses: this.mockExam.userResponses,
      correct_keys: this.mockExam.correctKeysMap,
      questions: this.mockExam.questions.map(q => ({
        id: q.id,
        q_index: q.q_index,
        question: q.question,
        option_a: q.option_a,
        option_b: q.option_b,
        option_c: q.option_c,
        option_d: q.option_d,
        shuffled_correct_key: q.shuffled_correct_key || this.mockExam.correctKeysMap[q.id],
        user_selected_key: this.mockExam.userResponses[q.id] || null,
        marks: q.marks || 2,
        chapter_code: q.chapter_code,
        section_group: q.section_group || '',
        topic: q.topic || '',
        difficulty: q.difficulty || 'Moderate',
        source_tag: q.source_tag || 'ICAI BoS Module'
      }))
    };

    try {
      this.showToast("Submitting and calculating score...", 'info');
      const res = await this.apiFetch('/api/submit-test', {
        method: 'POST',
        body: payload
      });
      const data = await res.json();

      if (data.success) {
        this.lastResult = data.result;
        this.renderTestResult();
        this.showTab('result');
        this.fetchStats();
        this.fetchQuestionBankCoverage();
      } else {
        this.showToast(data.error || "Submission failed", 'error');
      }
    } catch (err) {
      console.error(err);
      this.showToast("Network error submitting test", 'error');
    }
  },

  // =========================================================================
  // Test Results Review (Evaluated Across TOTAL Exam Questions)
  // =========================================================================

  renderTestResult() {
    if (!this.lastResult) return;
    const r = this.lastResult;

    const statusCard = document.getElementById('result-status-card');
    const title = document.getElementById('res-status-title');
    const subtitle = document.getElementById('res-status-subtitle');

    if (r.passed) {
      if (statusCard) statusCard.className = 'result-header-card passed';
      if (title) title.textContent = "QUALIFIED (PASSED)";
      if (subtitle) subtitle.textContent = "You met the mandatory 50% passing threshold across the complete examination.";
    } else {
      if (statusCard) statusCard.className = 'result-header-card failed';
      if (title) title.textContent = "NEEDS REVISION (BELOW 50%)";
      if (subtitle) subtitle.textContent = "Score is below the 50% cutoff computed across total questions. Review incorrect and skipped items below.";
    }

    const scoreDisp = document.getElementById('res-score-display');
    if (scoreDisp) scoreDisp.textContent = `${r.score} / ${r.max_marks} Marks`;

    const percentEl = document.getElementById('res-val-percent');
    if (percentEl) percentEl.textContent = `${r.percentage}%`;

    const totalQEl = document.getElementById('res-val-total-q');
    if (totalQEl) totalQEl.textContent = `${r.total_questions}`;

    const attemptedEl = document.getElementById('res-val-attempted');
    if (attemptedEl) attemptedEl.textContent = `${r.attempted}`;

    const unattemptedEl = document.getElementById('res-val-unattempted');
    if (unattemptedEl) unattemptedEl.textContent = `${r.unattempted}`;

    const correctEl = document.getElementById('res-val-correct');
    if (correctEl) correctEl.textContent = `${r.correct}`;

    const incorrectEl = document.getElementById('res-val-incorrect');
    if (incorrectEl) incorrectEl.textContent = `${r.incorrect}`;

    const mins = Math.floor((r.time_taken_seconds || 0) / 60);
    const secs = (r.time_taken_seconds || 0) % 60;
    const timeEl = document.getElementById('res-val-time');
    if (timeEl) timeEl.textContent = `${mins}m ${secs}s`;

    // Sectional breakdown
    if (r.sectional_breakdown) {
      const p1 = r.sectional_breakdown.part1;
      const p2 = r.sectional_breakdown.part2;

      const p1Label = document.getElementById('res-sec1-label');
      const p1Badge = document.getElementById('res-sec1-badge');
      const p1Bar = document.getElementById('res-sec1-bar');

      const p2Label = document.getElementById('res-sec2-label');
      const p2Badge = document.getElementById('res-sec2-badge');
      const p2Bar = document.getElementById('res-sec2-bar');

      if (this.currentSet === 'A') {
        if (p1Label) p1Label.textContent = "Part I: Corporate Laws (70 Marks)";
        if (p2Label) p2Label.textContent = "Part II: Economic Laws (30 Marks)";
      } else {
        if (p1Label) p1Label.textContent = "Part I: Strategic Cost Management (50 Marks)";
        if (p2Label) p2Label.textContent = "Part II: Strategic Performance Mgmt (50 Marks)";
      }

      if (p1Badge) p1Badge.textContent = `${p1.score} / ${p1.max_marks} (${p1.percentage}%)`;
      if (p1Bar) p1Bar.style.width = `${Math.min(100, p1.percentage)}%`;

      if (p2Badge) p2Badge.textContent = `${p2.score} / ${p2.max_marks} (${p2.percentage}%)`;
      if (p2Bar) p2Bar.style.width = `${Math.min(100, p2.percentage)}%`;
    }

    // Filter counts
    const fAll = document.getElementById('rev-filter-all');
    if (fAll) fAll.textContent = (r.questions || []).length;

    const fCorrect = document.getElementById('rev-filter-correct');
    if (fCorrect) fCorrect.textContent = r.correct;

    const fIncorrect = document.getElementById('rev-filter-incorrect');
    if (fIncorrect) fIncorrect.textContent = r.incorrect;

    const fUnattempted = document.getElementById('rev-filter-unattempted');
    if (fUnattempted) fUnattempted.textContent = r.unattempted;

    this.filterReview('all');
  },

  filterReview(filterType) {
    if (!this.lastResult || !this.lastResult.questions) return;
    const all = this.lastResult.questions;

    ['all', 'correct', 'incorrect', 'unattempted'].forEach(t => {
      const btn = document.getElementById(`btn-rev-${t}`);
      if (btn) btn.classList.toggle('active', t === filterType);
    });

    let filtered = all;
    if (filterType === 'correct') {
      filtered = all.filter(q => q.is_attempted && q.is_correct);
    } else if (filterType === 'incorrect') {
      filtered = all.filter(q => q.is_attempted && !q.is_correct);
    } else if (filterType === 'unattempted') {
      filtered = all.filter(q => !q.is_attempted);
    }

    this.renderReviewQuestions(filtered);
  },

  renderReviewQuestions(questionsList) {
    const container = document.getElementById('review-questions-list');
    if (!container) return;

    if (!questionsList || questionsList.length === 0) {
      container.innerHTML = `<div class="card" style="text-align: center; color: var(--text-muted); padding: 3rem;">No questions in this filter view.</div>`;
      return;
    }

    container.innerHTML = questionsList.map((q, idx) => {
      let badgeStatus = '';
      if (q.is_attempted) {
        if (q.is_correct) {
          badgeStatus = `<span class="review-badge-status correct">Correct (+${q.marks_awarded || 2} Marks)</span>`;
        } else {
          badgeStatus = `<span class="review-badge-status incorrect">Incorrect (Selected Option ${q.selected_option})</span>`;
        }
      } else {
        badgeStatus = `<span class="review-badge-status unattempted">Unattempted (0 Marks)</span>`;
      }

      const opts = [
        { k: 'A', text: q.option_a },
        { k: 'B', text: q.option_b },
        { k: 'C', text: q.option_c },
        { k: 'D', text: q.option_d }
      ];

      const optsHtml = opts.map(o => {
        const isCorrect = (o.k === q.correct_option);
        const isUserPick = (q.is_attempted && o.k === q.selected_option);

        let optClass = 'review-neutral';
        let badgeHtml = '';

        if (isUserPick && isCorrect) {
          optClass = 'review-correct';
          badgeHtml = `<span class="badge success" style="margin-left: auto;">Your Selection (Correct)</span>`;
        } else if (isUserPick && !isCorrect) {
          optClass = 'review-user-wrong';
          badgeHtml = `<span class="badge danger" style="margin-left: auto;">Your Selection (Incorrect)</span>`;
        } else if (!isUserPick && isCorrect) {
          optClass = 'review-correct';
          badgeHtml = `<span class="badge success" style="margin-left: auto;">Correct Answer</span>`;
        }

        return `
          <div class="option-item ${optClass}">
            <div class="option-letter">${o.k}</div>
            <div class="option-label">${o.text}</div>
            ${badgeHtml}
          </div>
        `;
      }).join('');

      return `
        <div class="review-question-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              ${badgeStatus}
              <span class="badge primary">${q.topic || q.chapter_code}</span>
              <span class="badge">${q.source_tag || 'ICAI BoS Module'}</span>
            </div>
            <span class="badge">${q.section_group || ''}</span>
          </div>

          <h4 style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1.25rem; font-weight: 600;">
            ${q.q_index || (idx + 1)}. ${q.question}
          </h4>

          <div class="options-container" style="margin-bottom: 1.25rem;">
            ${optsHtml}
          </div>

          <div class="explanation-box">
            <h6>Official Legal & Conceptual Rationale</h6>
            <p style="font-size: 0.92rem; line-height: 1.6; margin-bottom: 0.5rem; color: var(--text-main);">${q.explanation || 'Refer to the statutory module for standard guidance.'}</p>
            ${q.section_ref ? `<div style="font-size: 0.85rem; color: var(--accent-gold); font-weight: 600;">Statutory Provision: ${q.section_ref}</div>` : ''}
            ${q.exam_tip ? `<div class="exam-trap-box" style="margin-top: 0.5rem;"><span>Trap Alert: ${q.exam_tip}</span></div>` : ''}
          </div>
        </div>
      `;
    }).join('');
  },

  async toggleBookmark(mcqId) {
    try {
      const res = await this.apiFetch('/api/bookmark', {
        method: 'POST',
        body: { mcq_id: mcqId }
      });
      const data = await res.json();
      if (data.success) {
        this.showToast(data.is_bookmarked ? "Added to Starred" : "Removed from Starred", 'info');
        await this.fetchBookmarks();
        if (this.mockExam.active && this.activeTab === 'mock') {
          const starBtn = document.getElementById('curr-q-star-btn');
          if (starBtn) starBtn.classList.toggle('active', data.is_bookmarked === 1);
        }
        if (this.activeTab === 'mistakes' && this.currentMistakeFilter === 'starred') {
          this.filterMistakes('starred');
        }
      }
    } catch (err) {
      console.error(err);
      this.showToast("Failed to toggle bookmark", 'error');
    }
  },

  // =========================================================================
  // Question Studio & Research Ingestion Audit
  // =========================================================================

  openResearchModal() {
    const modal = document.getElementById('research-ingest-modal');
    if (modal) modal.classList.add('active');
  },

  closeResearchModal() {
    const modal = document.getElementById('research-ingest-modal');
    if (modal) modal.classList.remove('active');
  },

  async submitResearchLog() {
    const source_name = (document.getElementById('res-ingest-title')?.value || '').trim();
    const source_type = document.getElementById('res-ingest-type')?.value || 'YouTube SPOM Review';
    const author_or_channel = (document.getElementById('res-ingest-author')?.value || '').trim();
    const key_findings = (document.getElementById('res-ingest-summary')?.value || '').trim();
    const questions_extracted = 5;

    if (!source_name || !key_findings) {
      this.showToast("Please provide source title and key findings", 'warning');
      return;
    }

    try {
      const res = await this.apiFetch('/api/research/ingest', {
        method: 'POST',
        body: {
          set_name: this.currentSet,
          source_name,
          source_type,
          author_or_channel,
          key_findings,
          questions_extracted
        })
      });
      const data = await res.json();
      if (data.success) {
        this.showToast("Research entry logged successfully", 'success');
        this.closeResearchModal();
        this.loadResearchLogs();
      }
    } catch (err) {
      console.error(err);
      this.showToast("Failed to save research log", 'error');
    }
  },

  async loadResearchLogs() {
    const container = document.getElementById('research-log-table-body');
    if (!container) return;

    try {
      const res = await this.apiFetch(`/api/research/logs?set=${this.currentSet}`);
      const data = await res.json();
      if (data.success && data.data.length > 0) {
        container.innerHTML = data.data.map(r => `
          <tr>
            <td><strong>${r.source_name}</strong><br><small style="color: var(--text-dim);">${r.author_or_channel || 'Anonymous'}</small></td>
            <td><span class="badge primary">${r.source_type}</span></td>
            <td>${r.questions_extracted || 0} Qs</td>
            <td style="font-size: 0.85rem; color: var(--text-muted);">${r.key_findings}</td>
          </tr>
        `).join('');
      } else {
        container.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 2rem;">No research provenance records found.</td></tr>`;
      }
    } catch (err) {
      console.error("Error loading research logs:", err);
    }
  },

  async submitNewMCQ() {
    const question = (document.getElementById('new-mcq-question')?.value || '').trim();
    const chapter_code = document.getElementById('new-mcq-chapter')?.value;
    const topic = (document.getElementById('new-mcq-topic')?.value || '').trim();
    const option_a = (document.getElementById('new-mcq-opt-a')?.value || '').trim();
    const option_b = (document.getElementById('new-mcq-opt-b')?.value || '').trim();
    const option_c = (document.getElementById('new-mcq-opt-c')?.value || '').trim();
    const option_d = (document.getElementById('new-mcq-opt-d')?.value || '').trim();
    const correct_option = document.getElementById('new-mcq-correct')?.value;
    const explanation = (document.getElementById('new-mcq-exp')?.value || '').trim();
    const source_tag = (document.getElementById('new-mcq-source')?.value || '').trim() || 'Custom Added';

    if (!question || !option_a || !option_b || !option_c || !option_d) {
      this.showToast("Please fill in question text and all 4 options", 'warning');
      return;
    }

    try {
      const res = await this.apiFetch('/api/mcq', {
        method: 'POST',
        body: {
          set_name: this.currentSet,
          chapter_code,
          topic,
          question,
          option_a,
          option_b,
          option_c,
          option_d,
          correct_option,
          explanation,
          source_tag,
          section_group: this.currentSet === 'A' ? "Part I: Corporate Laws" : "Part I: Strategic Cost"
        })
      });
      const data = await res.json();
      if (data.success) {
        this.showToast("MCQ added to repository!", 'success');
        const form = document.getElementById('create-mcq-form');
        if (form) form.reset();
        this.fetchStats();
        this.loadQBQuestions();
      }
    } catch (err) {
      console.error(err);
      this.showToast("Failed to add question", 'error');
    }
  },

  async uploadCSV() {
    const fileInput = document.getElementById('bulk-file-input');
    if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
      this.showToast("Please choose a CSV file first", 'warning');
      return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    formData.append('set_name', this.currentSet);

    try {
      this.showToast("Uploading and validating questions...", 'info');
      const res = await this.apiFetch('/api/upload', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      if (data.success) {
        this.showToast(`Imported ${data.inserted} questions successfully!`, 'success');
        fileInput.value = '';
        this.fetchStats();
        this.loadQBQuestions();
      } else {
        this.showToast(data.error || "Upload failed", 'error');
      }
    } catch (err) {
      console.error(err);
      this.showToast("Error uploading file", 'error');
    }
  },

  async loadQBQuestions() {
    const tableBody = document.getElementById('qb-table-body');
    if (!tableBody) return;

    try {
      const res = await this.apiFetch(`/api/mcqs?set=${this.currentSet}&limit=50`);
      const data = await res.json();
      if (data.success) {
        this.qbQuestions = data.data;
        this.renderQBTable(this.qbQuestions);
      }
    } catch (err) {
      console.error(err);
    }
  },

  filterQBTable() {
    const search = (document.getElementById('qb-search-input')?.value || '').toLowerCase();
    const filtered = this.qbQuestions.filter(q => {
      const qText = (q.question || '').toLowerCase();
      const topicText = (q.topic || '').toLowerCase();
      return qText.includes(search) || topicText.includes(search);
    });
    this.renderQBTable(filtered);
  },

  renderQBTable(questions) {
    const tableBody = document.getElementById('qb-table-body');
    if (!tableBody) return;

    if (!questions || questions.length === 0) {
      tableBody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: var(--text-muted); padding: 2rem;">No questions match this filter.</td></tr>`;
      return;
    }

    tableBody.innerHTML = questions.map(q => `
      <tr>
        <td><span class="badge primary">${q.chapter_code}</span></td>
        <td style="max-width: 380px;">
          <div style="font-size: 0.92rem; font-weight: 500; margin-bottom: 0.25rem;">${q.question}</div>
          <small style="color: var(--text-dim);">${q.topic || ''}</small>
        </td>
        <td><span class="badge">${q.source_tag || 'ICAI'}</span></td>
        <td><strong style="color: var(--success); font-weight: 700;">Option ${q.correct_option}</strong></td>
        <td>
          <button class="btn btn-secondary btn-sm" onclick="app.deleteMCQ(${q.id})" style="color: var(--danger);">Delete</button>
        </td>
      </tr>
    `).join('');
  },

  async deleteMCQ(id) {
    if (!confirm("Are you sure you want to delete this question?")) return;
    try {
      const res = await this.apiFetch(`/api/mcq?id=${id}`, { method: 'DELETE' });
      const data = await res.json();
      if (data.success) {
        this.showToast("Question deleted", 'info');
        this.fetchStats();
        this.loadQBQuestions();
      }
    } catch (err) {
      console.error(err);
    }
  },

  // Toast Notification System
  showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'toastOut 0.3s forwards';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }
};

// Global Bootstrapper
document.addEventListener('DOMContentLoaded', () => {
  app.init();
});
