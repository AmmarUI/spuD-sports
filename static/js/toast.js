function showToast(title, message, type = 'normal', duration = 3000) {
  const el = document.getElementById('toast-component');
  const t = document.getElementById('toast-title');
  const m = document.getElementById('toast-message');
  if (!el) return;

  // Reset color state
  el.classList.remove(
    'bg-red-50','border-red-500','text-red-600',
    'bg-green-50','border-green-500','text-green-600',
    'bg-white','border-gray-300','text-gray-800'
  );

  if (type === 'success') {
    el.classList.add('bg-green-50','border-green-500','text-green-600');
    el.style.border = '1px solid #22c55e';
  } else if (type === 'error') {
    el.classList.add('bg-red-50','border-red-500','text-red-600');
    el.style.border = '1px solid #ef4444';
  } else {
    el.classList.add('bg-white','border-gray-300','text-gray-800');
    el.style.border = '1px solid #d1d5db';
  }

  t.textContent = title;
  m.textContent = message || '';

  el.style.transition = 'opacity 300ms, transform 300ms';
  el.style.opacity = '1';
  el.style.transform = 'translateY(0)';

  clearTimeout(el._hideTimer);
  el._hideTimer = setTimeout(() => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(16rem)'; 
  }, duration);
}
