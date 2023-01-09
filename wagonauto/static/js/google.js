const form = document.getElementById("pincode-form");
const pincodeInput = document.getElementById("pincode");
// Get a reference to the input field
const input = document.getElementById('pincode-input');

let postOfficeList = document.getElementById("post-office-list");
let pincode=0

form.addEventListener('submit', (event) => {
    // Prevent the form from being submitted
    event.preventDefault();

    // Get the value of the input field
    const pincode = input.value;

    // Store the pincode in local storage
    localStorage.setItem('pincode', pincode);

    // Call the searchAndDisplayCarShowrooms function
    searchAndDisplayCarShowrooms();
  });

  async function searchAndDisplayCarShowrooms() {
    // Get the pincode from local storage
    const pincode = localStorage.getItem('pincode');

    // Replace YOUR_API_KEY with your actual API key
    const API_KEY = 'AIzaSyAXmXks_i_gWF21TnqStIjtPGQ0Isa8wHs';

    // Replace YOUR_SEARCH_ENGINE_ID with the ID of your search engine
    const SEARCH_ENGINE_ID = '5647795047ae2441e';

    // Make a GET request to the Google Search API, passing in the pincode, search engine ID, and API key as query parameters
    const response = await fetch(`https://www.googleapis.com/customsearch/v1?q=${pincode}+car+showrooms+motors&cx=${SEARCH_ENGINE_ID}&key=${API_KEY}`);
    console.log(response)

    // Parse the response as JSON
    const data = await response.json();

    // Get a reference to the element where the search results will be displayed
    const resultsDiv = document.getElementById('results');

    // Clear the current contents of the results div
    resultsDiv.innerHTML = '';

    // Iterate through the search results and create a list item for each one
    for (const item of data.items) {
      const li = document.createElement('li');
      li.innerHTML = `<a href="${item.link}">${item.title}</a>`;
      resultsDiv.appendChild(li);
    }
  }
