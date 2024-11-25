const csrfToken = getCSRFToken();
const response = await fetch('http://127.0.0.1:8000/api/dj-rest-auth/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken,
  },
  body: JSON.stringify({
    username: formData.usernameOrEmail,
    password: formData.password
  }),
});


function getCSRFToken() {
  const cookies = document.cookie.split('; ');
  const csrfCookie = cookies.find(cookie => cookie.startsWith('csrftoken='));
  return csrfCookie ? csrfCookie.split('=')[1] : null;
}
