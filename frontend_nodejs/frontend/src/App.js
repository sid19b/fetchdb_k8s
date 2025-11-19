import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('/api/hello')   // relative path → Ingress will route it
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => setMessage('Error: ' + err.message));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '5rem' }}>
      <h1>Frontend (React + Nginx)</h1>
      <h2>Backend says: {message}</h2>
    </div>
  );
}

export default App;
