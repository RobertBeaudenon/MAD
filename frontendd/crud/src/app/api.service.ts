import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root",
})
export class ApiService {
  constructor(private http: HttpClient) {}

  base_url = " http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ "Content-type": "application/json" });

  getAllMovies(): Observable<any> {
    return this.http.get(this.base_url + "/movies/", {
      headers: this.httpHeaders,
    });
  }

  getOneMovie(id): Observable<any> {
    return this.http.get(this.base_url + "/movies/" + id + "/", {
      headers: this.httpHeaders,
    });
  }

  updateMovie(movie): Observable<any> {
    const body = { title: movie.title, desc: movie.desc, year: movie.year };
    return this.http.put(this.base_url + "/movies/" + movie.id + "/", body, {
      headers: this.httpHeaders,
    });
  }

  createMovie(movie): Observable<any> {
    const body = { title: movie.title, desc: movie.desc, year: movie.year };
    return this.http.post(this.base_url + "/movies/", body, {
      headers: this.httpHeaders,
    });
  }

  deleteMovie(id): Observable<any> {
    return this.http.delete(this.base_url + "/movies/" + id + "/", {
      headers: this.httpHeaders,
    });
  }
}
