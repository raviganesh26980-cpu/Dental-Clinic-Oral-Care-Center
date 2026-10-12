/* UpSense Dental — main.js (ES6) */
const root = document.documentElement;
/** Theme: saved choice > system preference */
root.dataset.theme = localStorage.getItem('theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
root.dir = localStorage.getItem('dir') || 'ltr';
document.addEventListener('DOMContentLoaded', () => {
  const flip = (key, attr, a, b) => { const v = root.getAttribute(attr) === a ? b : a; root.setAttribute(attr, v); localStorage.setItem(key, v); };
  document.getElementById('themeToggle')?.addEventListener('click', () => flip('theme', 'data-theme', 'light', 'dark'));
  document.getElementById('rtlToggle')?.addEventListener('click', () => flip('dir', 'dir', 'ltr', 'rtl'));
  const nav = document.getElementById('navToggle'), menu = document.getElementById('menu');
  nav?.addEventListener('click', () => nav.setAttribute('aria-expanded', menu.classList.toggle('open')));
  /** Skeleton loaders: swap for real fetch() when data comes from an API */
  setTimeout(() => document.querySelectorAll('.skeleton').forEach(e => e.classList.remove('skeleton')), 700);
  /** Client-side validation for forms[data-validate] */
  document.querySelectorAll('form[data-validate]').forEach(form => {
    form.addEventListener('submit', e => {
      let ok = true;
      form.querySelectorAll('[required]').forEach(f => {
        if (f.nextElementSibling?.classList.contains('field-error')) f.nextElementSibling.remove();
        f.classList.remove('invalid');
        if (!f.checkValidity()) {
          ok = false; f.classList.add('invalid');
          const m = document.createElement('span'); m.className = 'field-error'; m.setAttribute('role', 'alert');
          m.textContent = f.type === 'email' ? 'Enter a valid email address.' : f.type === 'tel' ? 'Enter a 10-digit phone number.' : 'This field is required.';
          f.after(m);
        }
      });
      if (!ok) e.preventDefault();
      else if (form.hasAttribute('data-demo')) { e.preventDefault(); form.innerHTML = '<p><strong>Thank you!</strong> We will call you to confirm your appointment.</p>'; }
    });
  });
});
