import { Component } from "@angular/core";
import { ApiService } from "./api.service";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
  providers: [ApiService],
})
export class AppComponent {
  movies = [{ title: "titanic" }, { title: "avatar" }];
  //object that i'm populating
  selectedMovie;

  constructor(private api: ApiService) {
    this.getMovies();
    //sets default fields
    this.selectedMovie = { id: -1, title: "", desc: "", year: 0 };
  }

  getMovies = () => {
    this.api.getAllMovies().subscribe(
      (data) => {
        this.movies = data;
      },
      (error) => {
        console.log(error);
      }
    );
  };

  movieClicked = (movie) => {
    console.log(movie.id);
    this.api.getOneMovie(movie.id).subscribe(
      (data) => {
        this.selectedMovie = data;
      },
      (error) => {
        console.log(error);
      }
    );
  };

  updateMovie = () => {
    this.api.updateMovie(this.selectedMovie).subscribe(
      (data) => {
        this.selectedMovie = data;
      },
      (error) => {
        console.log(error);
      }
    );
  };

  createMovie = () => {
    this.api.createMovie(this.selectedMovie).subscribe(
      (data) => {
        this.movies.push(data);
      },
      (error) => {
        console.log(error);
      }
    );
  };

  deleteMovie = () => {
    this.api.deleteMovie(this.selectedMovie.id).subscribe(
      (data) => {
        this.getMovies(); 
      },
      (error) => {
        console.log(error);
      }
    );
  };
}
