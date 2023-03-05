import { Box, Heading, Button } from '@chakra-ui/react';
import { CheckCircleIcon } from '@chakra-ui/icons';
import configService from "../services/config.js";
import { useNavigate } from "react-router-dom";

export default function PurchaseOk() {
  const navigate = useNavigate();

  const resetSubmit = () => {
    fetch(`${configService.apiReset}`)
      .then(data => {
        window.location.href = "/";
      })
      .catch(error => {
        console.error(error)
      })
  }
  return (
    <Box textAlign="center" spacing={{ base: 8, md: 14 }}
      py={{ base: 20, md: 36 }}>
      <CheckCircleIcon boxSize={'50px'} color={'purple.500'} />
      <Heading as="h2" size="xl" mt={6} mb={2}>
        Resetear la base de datos al estado actual
      </Heading>
      <Button colorScheme="purple" mt="5" onClick={() => resetSubmit()}>
        Resetear
      </Button>
    </Box>
  );
}
