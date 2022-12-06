// store the products in javscript object with title,dscription,dat,price,category,image and stock

// function to add the products to the list
function addProducts(title, description, date, price, category, image, stock) {
    // create a product object
    const product = {
        title: title,
        description: description,
        date: date,
        price: price,
        category: category,
        image: image,
        stock: stock
    }
    // add the product to the list
    products.push(product)
}

const products = [
    {
        title: "ATLP 1",
        description: "ATLP 1",
        date: "2021-01-01",
        price: 100,
        category: "ATLP",
        image: "https://images.unsplash.com/photo-1610078458449-8b8b1b2b1f1a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmFja2dyb3VuZCUyMGZpbGxlcnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80",
        stock: 10
    }
]
// add elements to products after submit
const form = document.getElementById("form");
form.addEventListener("submit", (e) => {
    // prevent the page from reloading
    e.preventDefault();
    // get the values from the form
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value;
    const price = document.getElementById("price").value;
    const category = document.getElementById("category").value;
    const image = document.getElementById("image").value;
    const stock = document.getElementById("stock").value;
    // create a object
    const product = {
        title,
        description,
        date,
        price,
        category,
        image,
        stock
    }
    // add the object to the products array
    products.push(product);
    // clear the form
    form.reset();
    // call the function to add the products to the list
    addProducts();


    console.log(products);
    console.log("product added");

    // reload the page to update products values
    location.reload();

});

// add the products to the list Id of the html
const productList = document.getElementById("productList");
// loop through the products
products.forEach(product => {
    // create a div element
    const div = document.createElement("div");
    // add the class to the div
    div.classList.add("product");
    // add the html to the div
    div.innerHTML = `
    <div class="product">
        <div class="product-image">
            <img src="${product.image}" alt="">
        </div>
        <div class="product-details">
            <div class="product-title">${product.title}</div>
            <div class="product-description">${product.description}</div>
        </div>
        <div class="product-price">${product.price}</div>
        <div class="product-stock">${product.stock}</div>
    </div>
    `;
    // add the div to the list
    productList.appendChild(div);
});
