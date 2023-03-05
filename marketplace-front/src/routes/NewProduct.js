import { Box, Button, Heading, Text, Container, Stack, Textarea, Input } from '@chakra-ui/react';
import { CheckCircleIcon, AddIcon } from '@chakra-ui/icons';
import { useRef, useState } from 'react';
import { useNavigate } from "react-router-dom";

import configService from "../services/config.js";


export default function NewProduct() {
  const navigate = useNavigate();

  const form = useRef(null);
  const [data, setData] = useState({
    name: "",
    description: "",
    price: "",
    image: ""
  });

  const handleChange = ({ currentTarget: input }) => {
    let newData = { ...data };
    newData[input.name] = input.value;
    setData(newData);
  };

  const handleImageChange = (e) => {
    let newData = { ...data };
    newData["image"] = e.target.files[0];
    setData(newData);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    let form_data = new FormData();
    if (data.image) {
      form_data.append('image', data.image, data.image.name);
    }
    form_data.append('name', data.name);
    form_data.append('description', data.description);
    form_data.append('price', data.price);

    fetch(`${configService.apiCreateProduct}`, {
      method: 'post',
      body: form_data
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        navigate("/addok");
      })
      .catch(error => {
        console.error(error)
      })
  }

  return (
    <Box textAlign="center" spacing={{ base: 8, md: 14 }}
      py={{ base: 20, md: 36 }}>
      <AddIcon boxSize={'50px'} color={'purple.500'} />
      <Heading as="h2" size="xl" mt={6} mb={2}>
        Nuevo producto
      </Heading>
      <Container>
        <form onSubmit={handleSubmit} ref={form}>
          <Stack spacing={3}>
            <Input placeholder='Nombre del producto' required id="name" name="name" onChange={handleChange} />
            <Input required placeholder='Precio' id="price" name="price" type="number" onChange={handleChange} />
            <Textarea placeholder='Descripción del producto' id="description" name="description" onChange={handleChange}></Textarea>
            <Box>
              <input required type="file" name="image" id="image" onChange={handleImageChange} />
            </Box>
            <Button type='submit'
              colorScheme='purple'>Guardar producto</Button>
          </Stack>
        </form>
      </Container>
    </Box>
  );
}
