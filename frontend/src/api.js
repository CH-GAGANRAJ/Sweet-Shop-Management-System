import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add a request interceptor to include the auth token in headers
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export const loginUser = async (username, password) => {
    const response = await api.post('/auth/login', { username, password });
    return response.data;
};

export const registerUser = async (username, email, password) => {
    const response = await api.post('/auth/register', { username, email, password });
    return response.data;
};

export const fetchSweets = async () => {
    const response = await api.get('/sweets/');
    return response.data;
};

export const addSweet = async (sweetData) => {
    const response = await api.post('/sweets/', sweetData);
    return response.data;
};

export const purchaseSweet = async (sweetId) => {
    const response = await api.post(`/sweets/${sweetId}/purchase`);
    return response.data;
};

export default api;
