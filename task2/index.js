const Ajv = require("ajv");
const ajv = new Ajv();
require("ajv-formats")(ajv);

// Define the JSON Schema
const schema = {
  type: "object",
  properties: {
    name: {type: "string"},
    surname: {type: "string"},
    email: { type: "string",format:"email"},
    dob: { type: "string",format:"date" },
    countryCode:{
        type: "string",
        enum: ["ESP","FR","PT","UK","USA"]
    }
  },
  required: ["name","surname","email","dob","countryCode"],
  additionalProperties: false
}

// Compile the schema
const validate = ajv.compile(schema)

const data = {
  name: "Luis",
  surname: "Patiño",
  email: "l.patino.c11@gmail.com",
  dob: "1999-11-07",
  countryCode: "ESP"
}

const valid = validate(data);
if (!valid) {
  console.log("The data are not valid:");
  console.log(validate.errors);
} else {
  console.log("The data are valid");
}