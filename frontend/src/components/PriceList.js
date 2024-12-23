
import React from 'react';
import PriceItem from './PriceItem';

const PriceList = ({ prices }) => {
  return (
    <ul className="space-y-4 max-w-3xl mx-auto">
      {prices.map((price, index) => (
        <PriceItem key={index} pair={price.pair} price={price.price} />
      ))}
    </ul>
  );
};

export default PriceList;
