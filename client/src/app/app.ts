import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DigitRecognition } from './pages/digit-recognition/digit-recognition';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, DigitRecognition],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('client');
}
