
import React from 'react';

const PriceItem = ({ pair, price }) => {
  return (
    <li className="flex justify-between items-center p-4 mb-2 bg-white rounded-lg shadow-md hover:bg-gray-50">
      <strong className="text-xl font-medium text-gray-800">{pair}</strong>
      <span className="text-xl text-green-500">{price}</span>
    </li>
  );
};

export default PriceItem;
