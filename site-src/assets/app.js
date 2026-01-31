const searchInput = document.querySelector('[data-search]');
const topicButtons = Array.from(document.querySelectorAll('[data-topic]'));
const cards = Array.from(document.querySelectorAll('[data-profile]'));
const resultsLabel = document.querySelector('[data-results]');

let activeTopic = 'all';

const updateResults = () => {
  if (!resultsLabel) return;
  const visible = cards.filter(card => card.style.display !== 'none');
  resultsLabel.textContent = `${visible.length} profiles`;
};

const applyFilters = () => {
  const query = (searchInput?.value || '').trim().toLowerCase();

  cards.forEach(card => {
    const name = (card.dataset.name || '').toLowerCase();
    const handle = (card.dataset.handle || '').toLowerCase();
    const topics = (card.dataset.topics || '').split(',').filter(Boolean);

    const matchesQuery = !query || name.includes(query) || handle.includes(query);
    const matchesTopic = activeTopic === 'all' || topics.includes(activeTopic);

    card.style.display = matchesQuery && matchesTopic ? '' : 'none';
  });

  updateResults();
};

if (searchInput) {
  searchInput.addEventListener('input', applyFilters);
}

topicButtons.forEach(button => {
  button.addEventListener('click', () => {
    topicButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
    activeTopic = button.dataset.topic || 'all';
    applyFilters();
  });
});

const revealElements = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealElements.forEach(el => observer.observe(el));
} else {
  revealElements.forEach(el => el.classList.add('is-visible'));
}

applyFilters();
