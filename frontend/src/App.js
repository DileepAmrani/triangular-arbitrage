

import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import PriceList from './components/PriceList';

const App = () => {
  const [prices, setPrices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [update, setUpdate] = useState('');

  useEffect(() => {
    const fetchPrices = async () => {
      try {
        const response = await fetch('https://triangular-arbitrage-backend.vercel.app/prices');
        const data = await response.json();
        setUpdate(data);

        const pricesArray = Object.entries(data.prices).map(([pair, price]) => ({
          pair,
          price,
        }));

        setPrices(pricesArray);
      } catch (error) {
        console.error('Error fetching prices:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPrices();
  }, [update]);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <Header />
      <div className="mt-6 text-center">
        <h1 className="text-3xl font-semibold text-blue-600 ">Binance Price Tracker</h1>
      </div>

      <div className="mt-6">
        {loading ? (
          <p className="text-xl text-gray-700 text-center">Loading prices...</p>
        ) : (
          Array.isArray(prices) && prices.length > 0 ? (
            <PriceList prices={prices} />
          ) : (
            <p className="text-xl text-red-500 text-center">No prices available.</p>
          )
        )}
      </div>
    </div>
  );
};

export default App;
