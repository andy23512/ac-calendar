import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';
import { Observable } from 'rxjs';
import { CategoryType } from '@frontend/interface';
import { map } from 'rxjs/operators';

@Component({
  selector: 'frontend-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  public data$: Observable<CategoryType[]>;
  constructor(private dataService: DataService) {}
  public ngOnInit() {
    this.data$ = this.dataService
      .watchQueryAllData()
      .valueChanges.pipe(map(r => r.data.categories));
  }
}
