import {
  Box,
  Heading,
  Container,
  Text,
  Badge
} from '@chakra-ui/react';

import { useState, useEffect } from "react";
import configService from "../services/config.js";

import { ProductCard } from '../components/ProductCard'
import { ProductGrid } from '../components/ProductGrid'

export default function Products() {
  const [products, setProducts] = useState([]);
  let user = JSON.parse(localStorage.getItem('user'));

  if (window.localStorage.getItem("user") === null) {
    window.location.href = "/";
  } else {
    fetch(`${configService.apiGetBuyers}?uuid=${user.user}`, {
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        if (data.count === 0) {
          // Borramos el existente en localstorage y creamos uno nuevo
          localStorage.clear();
          window.location.href = "/";
        } else {
          // Actualizamos el usuario en localstorage
          localStorage.clear();
          window.localStorage.setItem("user", JSON.stringify({
            user: data.results[0].uuid,
            coins: data.results[0].coins,
          }));
        }
      })
      .catch(error => {
        console.error(error)
      })
  }

  useEffect(() => {
    if (window.localStorage.getItem("user") === null) {
      window.location.href = "/";
    }
    let user = JSON.parse(localStorage.getItem('user'));
    fetch(`${configService.apiGetBuyers}?uuid=${user.user}`, {
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        if (data.count === 0) {
          // Borramos el existente en localstorage y creamos uno nuevo
          localStorage.clear();
          window.location.href = "/";
        } else {
          // Actualizamos el usuario en localstorage
          localStorage.clear();
          window.localStorage.setItem("user", JSON.stringify({
            user: data.results[0].uuid,
            coins: data.results[0].coins,
          }));
        }
      })
      .catch(error => {
        console.error(error)
      })

    console.log(configService.apiGetProducts);
    fetch(`${configService.apiGetProducts}`)
      .then((res) => res.json())
      .then(
        (res) => {
          setProducts(res.results);
        },
        (error) => {
          console.log(error);
        }
      );
  }, [setProducts]);

  return (
    <>
      <Box>
        <Container maxW={'6xl'} py={5}>
          <Heading as="h1" size="xl" mt={6} mb={6} textAlign="center" spacing={{ base: 8, md: 14 }}>
            Productos
          </Heading>
          <Box textAlign="center" mt={6} mb={6}>
            <Badge fontSize='1.2em' colorScheme='purple'>Monedas: {JSON.parse(localStorage.getItem('user')).coins}</Badge>
          </Box>
          <ProductGrid>
            {products.map((product) => (
              <ProductCard key={product.pk} product={product} />
            ))}
          </ProductGrid>
        </Container>
      </Box>
    </>
  );
}
