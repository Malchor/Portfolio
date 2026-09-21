import 'dart:io';


class Product {
  String name;
  double price;
  bool clubcardItem;

  Product(this.name, this.price, {this.clubcardItem = false});

  double getPrice({bool hasClubcard = false}) {
    if (clubcardItem && hasClubcard) {
      return price * 0.85;
    }
    return price;
  }

  String toString() {
    return "$name: £$price";
  }
}


class ShoppingCart {
  List<Product> _items = [];
  bool hasClubcard;

  ShoppingCart({this.hasClubcard = false});

  void addProduct(Product product) {
    _items.add(product);
  }

  double getTotal() {
    double total = 0;
    for (var item in _items) {
      total += item.getPrice(hasClubcard: hasClubcard);
    }
    return total;
  }

  String toString() {
    String result = "Shopping cart:\n";
    for (var item in _items) {
      result += "  ${item.name}: £${item.price}\n";
    }
    result += "Total: £${getTotal().toStringAsFixed(2)}";
    return result;
  }
}


class User {
  String username;
  String _password = "default123";

  User(this.username);

  bool changePassword(String currentPassword, String newPassword) {
    if (_password == currentPassword) {
      _password = newPassword;
      return true;
    }
    return false;
  }

  bool login(String password) {
    return _password == password;
  }

  String toString() {
    return username;
  }
}


class Post {
  String content;
  String author;
  int date;
  int likes = 0;

  Post(this.content, this.author, this.date);

  void like() {
    likes++;
  }

  String toString() {
    return "$date - $author: $content (Likes: $likes)";
  }
}

class SocialMediaFeed {
  List<Post> _posts = [];

  void addPost(Post post) {
    _posts.add(post);
  }

  void removePost(Post post) {
    _posts.remove(post);
  }

  void likePost(Post post) {
    post.like();
  }

  void displayFeed() {
    _posts.sort((a, b) => a.date.compareTo(b.date));
    for (var post in _posts) {
      print(post);
    }
  }
}
  
abstract class netContent {
  String title;
  bool watched = false;

  netContent(this.title);

  void markWatched() {
    watched = true;
  }

  String toString() {
    return watched ? "$title (Watch It Again)" : title;
  }
}

class Movie extends netContent {
  int duration;

  Movie(String title, this.duration) : super(title);

  String toString() {
    return "${watched ? "$title (Watch It Again)" : title} - $duration mins";
  }
}

class Series extends netContent {
  List<List<bool>> seasons;

  Series(String title, int numSeasons, int episodesPerSeason)
      : seasons = List.generate(
            numSeasons,
            (_) => List.generate(episodesPerSeason, (_) => false)),
        super(title);

  void watchEpisode(int season, int episode) {
    seasons[season][episode] = true;

    watched = seasons.every(
      (season) => season.every((episode) => episode),
    );
  }

  String toString() {
    return watched ? "$title (Watch It Again)" : title;
  }
}

class NetflixCollection {
  List<netContent> _content = []; 

  void addContent(netContent c) { 
    _content.add(c);
  }

  void showAll() {
    for (var c in _content) {
      print(c);
    }
  }
}

void main() {
  var movie1 = Movie("Inception", 148);
  var series1 = Series("Stranger Things", 2, 3);

  var collection = NetflixCollection();

  collection.addContent(movie1);
  collection.addContent(series1);

  movie1.markWatched();

  series1.watchEpisode(0, 0);
  series1.watchEpisode(0, 1);
  series1.watchEpisode(0, 2);
  series1.watchEpisode(1, 0);
  series1.watchEpisode(1, 1);
  series1.watchEpisode(1, 2);

  collection.showAll();


  var cart = ShoppingCart();
  cart._items;
}
