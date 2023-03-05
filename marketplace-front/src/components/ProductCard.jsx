import {
  AspectRatio,
  Box,
  Button,
  Image,
  Skeleton,
  Stack,
  Text,
  useColorModeValue,
} from '@chakra-ui/react'
import { PriceTag } from './PriceTag'

import configService from "../services/config.js";
import { useNavigate } from "react-router-dom";


export const ProductCard = (props) => {
  const { product, rootProps } = props
  const navigate = useNavigate();

  const buy = (product_pk, product_price, product_purchased) => {
    let user = JSON.parse(localStorage.getItem('user'));
    if (user.coins < product_price) {
      alert("No tienes suficientes monedas para comprar este producto");
      return false;
    }

    let form_data = new FormData();
    form_data.append('buyer_uuid', user.user);
    form_data.append('product_pk', product_pk);

    fetch(`${configService.apiBuyProduct}${user.user}/`, {
      method: 'post',
      body: form_data
    })
      .then(data => {
        console.log(data);
        window.localStorage.setItem("user", JSON.stringify({
          user: user.user,
          coins: user.coins - product_price,
        }));
        navigate("/purchaseok");
      })
      .catch(error => {
        console.error(error)
      })
  };


  return (
    <Stack
      spacing={{
        base: '4',
        md: '7',
      }}
      {...rootProps}
    >
      <Box position="relative">
        <AspectRatio ratio={4 / 4}>
          <Image
            src={product.image}
            alt={product.name}
            draggable="false"
            fallback={<Skeleton />}
            borderRadius={{
              base: 'md',
              md: 'xl',
            }}
          />
        </AspectRatio>
      </Box>
      <Stack>
        <Stack spacing="1">
          <Text fontWeight="medium" color={useColorModeValue('gray.700', 'gray.400')}>
            {product.name}
          </Text>
          <PriceTag price={product.price} currency="USD" />
        </Stack>
      </Stack>
      <Box mt="auto">
        <Stack align="center" >
          {!product.purchased && (
            <Button colorScheme="purple" width="full" onClick={() => buy(product.pk, product.price, product.purchased)}>
              Comprar
            </Button>
          )}
        </Stack>
      </Box>
    </Stack>
  )
}
