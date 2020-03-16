import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { WebradioComponent } from './webradio/webradio.component';


const routes: Routes = [
  { path: 'homepage', component: HomepageComponent },
  { path: 'webradios', component: WebradioComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
