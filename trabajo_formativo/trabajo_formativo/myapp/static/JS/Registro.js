
     
function togglePassword(inputId) {
    var input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
  }
  
  document.getElementById('registroForm').addEventListener('submit', function(event) {
    var nombreCompleto = document.getElementById('NombreCompleto').value.trim();
    var nombreUsuario = document.getElementById('NombreUsuario').value.trim();
    var correoElectronico = document.getElementById('CorreoElectronico').value.trim();
    var claveAcceso = document.getElementById('ClaveAcceso').value.trim();
    var repiteClave = document.getElementById('RepiteClave').value.trim();
    var fechaNacimiento = document.getElementById('FechaNacimiento').value.trim();
    var direccionDespacho = document.getElementById('DireccionDespacho').value.trim();
  
    if (!nombreCompleto || !nombreUsuario || !correoElectronico || !claveAcceso || !repiteClave || !fechaNacimiento) {
        alert('Por favor, complete todos los campos.');
        event.preventDefault();
        return;
    }
  
    
    if (nombreCompleto.length <= 6) {
        alert('El nombre completo debe tener más de 6 caracteres.');
        event.preventDefault();
        return;
    }


    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(correoElectronico)) {
        alert('Por favor, ingrese un correo electrónico válido.');
        event.preventDefault();
        return;
    }
  
    var passwordRegex = /^(?=.*\d)(?=.*[A-Z]).{6,18}$/;
    if (!passwordRegex.test(claveAcceso)) {
        alert('La contraseña debe tener al menos un número y una letra en mayúscula, y tener entre 6 y 18 caracteres.');
        event.preventDefault();
        return;
    }
    
    if (claveAcceso !== repiteClave) {
        alert('Las contraseñas no coinciden.');
        event.preventDefault();
        return;
    }
  
    var hoy = new Date();
    var fechaNacimientoDate = new Date(fechaNacimiento);
    var edad = hoy.getFullYear() - fechaNacimientoDate.getFullYear();
    var mes = hoy.getMonth() - fechaNacimientoDate.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimientoDate.getDate())) {
        edad--;
    }
    if (edad < 13) {
        alert('Debe tener al menos 13 años para registrarse en el sitio web.');
        event.preventDefault();
        return;
    }
    
   
    alert('¡Felicidades, has sido registrado satisfactoriamente! Por favor, revisa tu correo electrónico para confirmar tus datos.');
  });
  