let base = "";
if (window.location.hostname.indexOf("localhost") > -1) {
  base = "http://localhost:8000";
} else {
  base = "http://conquermarket.34018.net:8000";
}

const baseUrlApi = `${base}/`;

const configService = {
  apiGetProducts: `${baseUrlApi}products/`,
  apiCreateProduct: `${baseUrlApi}createproduct/`,
  apiGetBuyers: `${baseUrlApi}buyers/`,
  apiBuyProduct: `${baseUrlApi}myproducts/`,
  apiReset: `${baseUrlApi}reset/`,
};

export default configService;
