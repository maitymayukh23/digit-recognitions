import { Component } from '@angular/core';
import { Slate } from '../../components/slate/slate';
import { Api } from '../../services/api';

@Component({
  selector: 'app-digit-recognition',
  imports: [Slate],
  templateUrl: './digit-recognition.html',
  styleUrl: './digit-recognition.css'
})
export class DigitRecognition {
  predictionResponse: object| null = null;
  constructor(private api: Api) {}
  onGridChange(grid: number[]){
    console.log(grid);
    this.api.getPrediction(grid).then(response => {
      this.predictionResponse = response;
      console.log(response);
    });
  }

}
