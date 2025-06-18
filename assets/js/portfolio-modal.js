// Portfolio Modal JS
function openPortfolioModal(id) {
  document.getElementById('modal-' + id).style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function closePortfolioModal(id) {
  document.getElementById('modal-' + id).style.display = 'none';
  document.body.style.overflow = '';
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.portfolio-modal .close').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const modal = btn.closest('.portfolio-modal');
      if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  });
  document.querySelectorAll('.portfolio-modal').forEach(function(modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  });
}); 