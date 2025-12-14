import React, { useState, useEffect } from 'react';
import { fetchSweets, addSweet, purchaseSweet } from './api';

const Sweets = () => {
    const [sweets, setSweets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // Form state for adding new sweet
    const [newSweet, setNewSweet] = useState({
        name: '',
        category: '',
        price: '',
        quantity: ''
    });
    const [addLoading, setAddLoading] = useState(false);

    const loadSweets = async () => {
        try {
            const data = await fetchSweets();
            setSweets(data);
        } catch (err) {
            console.error("Failed to fetch sweets", err);
            setError("Failed to load sweets.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadSweets();
    }, []);

    const handleAddChange = (e) => {
        setNewSweet({
            ...newSweet,
            [e.target.name]: e.target.value
        });
    };

    const handleAddSubmit = async (e) => {
        e.preventDefault();
        setAddLoading(true);
        setError('');

        try {
            // Validate and types
            const payload = {
                name: newSweet.name,
                category: newSweet.category || "General",
                price: parseFloat(newSweet.price),
                quantity: parseInt(newSweet.quantity)
            };

            await addSweet(payload);
            setNewSweet({ name: '', category: '', price: '', quantity: '' });
            await loadSweets(); // Reload list
        } catch (err) {
            console.error(err);
            setError("Failed to add sweet. Check inputs.");
        } finally {
            setAddLoading(false);
        }
    };

    const handlePurchase = async (id) => {
        try {
            await purchaseSweet(id);
            // Optimistic update or reload
            await loadSweets();
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Purchase failed");
        }
    };

    if (loading) return <div className="text-center">Loading sweets...</div>;

    return (
        <div>
            {/* Add Sweet Section */}
            <div className="glass-card add-sweet-section">
                <h3>Add New Sweet</h3>
                <form onSubmit={handleAddSubmit} className="add-sweet-form">
                    <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Name</label>
                        <input
                            name="name"
                            value={newSweet.name}
                            onChange={handleAddChange}
                            required
                            placeholder="Sweet Name"
                        />
                    </div>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Category</label>
                        <input
                            name="category"
                            value={newSweet.category}
                            onChange={handleAddChange}
                            placeholder="e.g. Traditional"
                        />
                    </div>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Price</label>
                        <input
                            name="price"
                            type="number"
                            step="0.01"
                            value={newSweet.price}
                            onChange={handleAddChange}
                            required
                            placeholder="0.00"
                        />
                    </div>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Quantity</label>
                        <input
                            name="quantity"
                            type="number"
                            value={newSweet.quantity}
                            onChange={handleAddChange}
                            required
                            placeholder="0"
                        />
                    </div>
                    <button type="submit" className="btn btn-action" disabled={addLoading}>
                        {addLoading ? 'Adding...' : 'Add to Inventory'}
                    </button>
                </form>
                {error && <p className="error-msg" style={{ marginTop: '10px' }}>{error}</p>}
            </div>

            {/* Sweets Grid */}
            <h2 style={{ marginBottom: '1rem' }}>Available Sweets</h2>
            <div className="sweets-container">
                {sweets.map(sweet => (
                    <div key={sweet.id} className="glass-card sweet-card">
                        <div className="sweet-info">
                            <h3>{sweet.name}</h3>
                            <div className="sweet-meta">
                                <span>{sweet.category}</span>
                                <span style={{ color: sweet.quantity > 0 ? '#2ed573' : '#ff4757' }}>
                                    {sweet.quantity > 0 ? `${sweet.quantity} in stock` : 'Out of Stock'}
                                </span>
                            </div>
                            <p>Delicious handmade {sweet.name.toLowerCase()}.</p>
                        </div>

                        <div>
                            <div className="price-tag">${sweet.price.toFixed(2)}</div>
                            <button
                                className="btn btn-primary w-100"
                                onClick={() => handlePurchase(sweet.id)}
                                disabled={sweet.quantity <= 0}
                            >
                                {sweet.quantity > 0 ? 'Purchase One' : 'Sold Out'}
                            </button>
                        </div>
                    </div>
                ))}
                {sweets.length === 0 && <p className="text-center w-100">No sweets available yet.</p>}
            </div>
        </div>
    );
};

export default Sweets;
