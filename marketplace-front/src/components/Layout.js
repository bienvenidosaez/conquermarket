import {
  Link as RouteLink,
  Outlet
} from "react-router-dom";

import Header from './Header.js';
import Menu from './Menu.js';
import Footer from './Footer.js';

export default function Layout() {
  let paisa = 5000;
  return (
    <>
      <Menu />
      <Outlet />
      <Footer />
    </>
  );
}
