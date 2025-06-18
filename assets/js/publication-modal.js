// Publication Modal JS
function openPublicationModal(id) {
  document.getElementById('modal-' + id).style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function closePublicationModal(id) {
  document.getElementById('modal-' + id).style.display = 'none';
  document.body.style.overflow = '';
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.publication-modal .close').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const modal = btn.closest('.publication-modal');
      if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  });
  // Optional: close modal when clicking outside the modal content
  document.querySelectorAll('.publication-modal').forEach(function(modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  });
}); 