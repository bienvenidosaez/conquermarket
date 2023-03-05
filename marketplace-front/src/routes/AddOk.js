import { Box, Heading, Button } from '@chakra-ui/react';
import { CheckCircleIcon } from '@chakra-ui/icons';
import { Link as RouterLink } from 'react-router-dom';

export default function PurchaseOk() {
  return (
    <Box textAlign="center" spacing={{ base: 8, md: 14 }}
      py={{ base: 20, md: 36 }}>
      <CheckCircleIcon boxSize={'50px'} color={'purple.500'} />
      <Heading as="h2" size="xl" mt={6} mb={2}>
        Producto añadido correctamente
      </Heading>
      <RouterLink to="/products">
        <Button colorScheme="purple" mt="5">
          Volver a los productos
        </Button>
      </RouterLink>
    </Box>
  );
}
