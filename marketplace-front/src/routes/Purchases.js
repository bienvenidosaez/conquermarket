import {
  Box,
  Heading,
  Container,
  Button
} from '@chakra-ui/react';
import { v4 as uuidv4 } from 'uuid';
import { Link as RouterLink } from 'react-router-dom';

import { useState, useEffect } from "react";
import configService from "../services/config.js";
import { useNavigate } from "react-router-dom";

import { ProductCard } from '../components/ProductCard'
import { ProductGrid } from '../components/ProductGrid'

export default function Products() {
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();

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

    fetch(`${configService.apiBuyProduct}${user.user}/`)
      .then((res) => res.json())
      .then(
        (res) => {
          setProducts(res.products);
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
            Mis Compras
          </Heading>
          <ProductGrid>
            {products.map((product) => (
              <ProductCard key={product.pk} product={product} />
            ))}
            {products.length === 0 && (
              <Box textAlign="center" mt={6} mb={6}>
                <Heading as="h2" size="lg" mt={6} mb={6} textAlign="center" spacing={{ base: 8, md: 14 }}>
                  No has comprado nada aún
                </Heading>
                <RouterLink to="/products">
                  <Button colorScheme="purple" mt="5">
                    Mira los productos disponibles
                  </Button>
                </RouterLink>
              </Box>
            )}
          </ProductGrid>
        </Container>
      </Box>
    </>
  );
}
