console.log("hello world");

function validateCertificateFields(
  cn,
  organization,
  city,
  state,
  country
) {
  // check cn field
  if (
    validator.isEmpty(cn) ||
    !validator.isLength(cn, { min: 3, max: 64 }) ||
    !validator.isAlphanumeric(cn)
  ) {
    return {
      isValid: false,
      message: "Invalid Common Name",
    };
  }

  // check organization field
  if (
    validator.isEmpty(organization) ||
    !validator.isLength(organization, { min: 3, max: 64 }) ||
    !validator.isAlphanumeric(organization)
  ) {
    return {
      isValid: false,
      message: "Invalid Organization",
    };
  }

  // check city field
  if (
    validator.isEmpty(city) ||
    !validator.isLength(city, { min: 3, max: 64 }) ||
    !validator.isAlphanumeric(city)
  ) {
    return {
      isValid: false,
      message: "Invalid City",
    };
  }

  // check state field
  if (
    validator.isEmpty(state) ||
    !validator.isLength(state, { min: 3, max: 64 }) ||
    !validator.isAlphanumeric(state)
  ) {
    return {
      isValid: false,
      message: "Invalid State",
    };
  }

  // check country field
  if (
    validator.isEmpty(country) ||
    !validator.isLength(country, { min: 3, max: 64 }) ||
    !validator.isAlphanumeric(country)
  ) {
    return {
      isValid: false,
      message: "Invalid Country",
    };
  }

  return true;
}

// form
const form = document.getElementById("csr-form");
const submitBtn = document.getElementById("submit-btn");

// form fields
const cn = document.getElementById("cn");
const organization = document.getElementById("organization");
const city = document.getElementById("city");
const state = document.getElementById("state");
const country = document.getElementById("country");

// error message
const errorMsg = document.getElementById("error-msg");

// form validation
form.addEventListener("submit", (e) => {
  e.preventDefault();

  // validate form fields
  const isValid = validateCertificateFields(
    cn.value,
    organization.value,
    city.value,
    state.value,
    country.value
  );

  if (isValid === true) {
    // submit form
    console.log("submit form");
  } else {
    // show error message
    errorMsg.classList.remove("hidden");
    errorMsg.textContent = isValid.message;
  }
});
