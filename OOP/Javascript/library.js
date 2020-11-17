class Person {
    constructor(name) {
        this.name = name;
    }
}

class Librarian extends Person { }

class Book {
    constructor(properties) {
        this.name = properties.name;
        this.isbn = properties.isbn;
        this.author = properties.author;
    }
}

class Shelf {
    constructor(shelf_id) {
        this.shelf_id = shelf_id;
        this.books = {};
    }
    
    addBook(book) {
        if(!this.books.hasOwnProperty(book.isbn)) {
            this.books[book.isbn] = [];
        }
        this.books[book.isbn].push(book)
    }
}

class Library {
    constructor(name, librarian) {
        this.name = name;
        this.librarian = librarian;
        this.shelves = [];
        this.furniture = [];
        this.numberOfBooks = 0;
    }
    
    addBook(shelf_id, book) {
        var shelf = this.shelves[shelf_id];
        if(shelf) {
            if(book instanceof Book) {
                shelf.addBook(book);
                this.numberOfBooks++;
            }
        } else {
            console.log("That shelf does not exist");
        }
    }
    
    addShelf() {
        var id = this.shelves.length;
        var shelf = new Shelf(id)
        this.shelves.push(shelf)
    }
}

var chidi = new Librarian("Chidiebere");
var andelaLibrary = new Library("Amity", chidi);
console.log("Before", andelaLibrary)
andelaLibrary.addShelf()
console.log("After", andelaLibrary)

var book = new Book({
    name: "Beasts of no Nation",
    author: "Uzo Okonjo-Iweala",
    isbn: "11111-1111-11111"
})

andelaLibrary.addBook(0, book)
andelaLibrary.addBook(0, book)
console.log("After adding book", andelaLibrary)
console.log(andelaLibrary.shelves[0])
