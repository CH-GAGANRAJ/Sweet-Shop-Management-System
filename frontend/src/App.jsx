import React, { useState, useEffect } from 'react';
import Login from './Login';
import Sweets from './Sweets';
import './style.css'; // Importing global styles

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'));

    useEffect(() => {
        // Sync state with local storage on mount (already done in useState default)
        // You could also validate the token here if you had a /me endpoint
    }, []);

    const handleLogin = (newToken) => {
        localStorage.setItem('token', newToken);
        setToken(newToken);
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        setToken(null);
    };

    return (
        <div id="app-root">
            {token ? (
                <>
                    <nav className="glass-card nav-header">
                        <h2 style={{ margin: 0 }}>Sweet Shop Admin</h2>
                        <button className="btn btn-secondary" onClick={handleLogout}>
                            Logout
                        </button>
                    </nav>
                    <main>
                        <Sweets />
                    </main>
                </>
            ) : (
                <>
                    <h1>Sweet Shop Management</h1>
                    <Login onLogin={handleLogin} />
                </>
            )}
        </div>
    );
}

export default App;
