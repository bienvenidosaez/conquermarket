import {
  Box,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Icon,
  useColorModeValue,
} from '@chakra-ui/react';
import { useState, useEffect } from 'react';

import {
  Link as RouteLink
} from "react-router-dom";

// import User from '../utils/User.js';
import { v4 as uuidv4 } from 'uuid';

import configService from "../services/config.js";

export default function Home(props) {
  const [user, setUser] = useState({
    user: 'Cargando...',
    coins: 'Cargando...'
  });

  const getOrCreateUser = () => {
    let newUuid = uuidv4();
    let newCoins = 5000;
    let form_data = new FormData();

    if (window.localStorage.getItem("user") === null) {
      form_data = new FormData();
      form_data.append('uuid', newUuid);

      fetch(`${configService.apiGetBuyers}`, {
        method: 'post',
        body: form_data
      })
        .then(response => response.json())
        .then(data => {
          console.log(data)
          console.log('Se crea porque localstorage estaba vacía');
          window.localStorage.setItem("user", JSON.stringify({
            user: data.uuid,
            coins: data.coins
          }));
          setUser(JSON.parse(window.localStorage.getItem("user")));
        })
        .catch(error => {
          console.error(error)
        })

    } else {
      let user = JSON.parse(window.localStorage.getItem("user"));
      // Comprobamos que el usuario existe en la base de datos
      fetch(`${configService.apiGetBuyers}?uuid=${user.user}`, {
      })
        .then(response => response.json())
        .then(data => {
          console.log(data)
          if (data.count === 0) {
            // Borramos el existente en localstorage y creamos uno nuevo
            localStorage.clear();
            form_data = new FormData();
            form_data.append('uuid', newUuid);
            fetch(`${configService.apiGetBuyers}`, {
              method: 'post',
              body: form_data
            })
              .then(response => response.json())
              .then(data => {
                console.log(data)
                console.log('Se crea porque existía en local y no en la bd');

                window.localStorage.setItem("user", JSON.stringify({
                  user: data.uuid,
                  coins: data.coins
                }));
                setUser(JSON.parse(window.localStorage.getItem("user")));
              })
              .catch(error => {
                console.error(error)
              })
          } else {
            // Actualizamos el usuario en localstorage
            localStorage.clear();
            window.localStorage.setItem("user", JSON.stringify({
              user: data.results[0].uuid,
              coins: data.results[0].coins,
            }));
            setUser(JSON.parse(window.localStorage.getItem("user")));
          }
        })
        .catch(error => {
          console.error(error)
        })
    }
    console.log('se ejecuta getOrCreateUser');
  }

  useEffect(() => {
    getOrCreateUser();
  }, []);

  return (
    <>
      <Container maxW={'3xl'}>
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 8, md: 14 }}
          py={{ base: 20, md: 36 }}>
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '5xl' }}
            lineHeight={'110%'}>
            Bienvenido al MarketPlace de<br />
            <Text as={'span'} color={'purple.400'}>
              Conquer Blocks
            </Text>
          </Heading>
          <Text>
            Usuario: <strong>{user.user}</strong><br />
            Saldo: <strong>{user.coins}</strong><br />
          </Text>
          <Stack
            direction={'column'}
            spacing={3}
            align={'center'}
            alignSelf={'center'}
            position={'relative'}>
            <RouteLink to="/products">
              <Button
                colorScheme={'purple'}
                bg={'purple.400'}
                rounded={'full'}
                px={6}
                _hover={{
                  bg: 'purple.500',
                }}>
                Ver productos
              </Button>
            </RouteLink>
          </Stack>
        </Stack>
      </Container>
    </>
  );
}
