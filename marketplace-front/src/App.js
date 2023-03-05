import React from 'react';
import {
  ChakraProvider,
  theme,
} from '@chakra-ui/react';

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Outlet,
} from "react-router-dom";

import Layout from './components/Layout.js';
import Home from './routes/Home';
import Products from './routes/Products';
import Purchases from './routes/Purchases';
import PurchaseOk from './routes/PurchaseOk';
import AddOk from './routes/AddOk';
import Reset from './routes/Reset';
import NewProduct from './routes/NewProduct';
import ErrorPage from './routes/ErrorPage.js';

export default function App() {

  return (
    <ChakraProvider theme={theme}>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="products" element={<Products />} />
          <Route path="purchases" element={<Purchases />} />
          <Route path="addok" element={<AddOk />} />
          <Route path="purchaseok" element={<PurchaseOk />} />
          <Route path="newproduct" element={<NewProduct />} />
          <Route path="reset" element={<Reset />} />
          <Route path="*" element={<ErrorPage />} />
        </Route>
      </Routes>
    </ChakraProvider>
  );
}
