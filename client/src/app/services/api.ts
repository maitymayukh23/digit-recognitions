import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class Api {
  async getPrediction(matrix: number[]): Promise<any> {
    try {
      const response = await axios.post('http://127.0.0.1:4201/predict', { matrix });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        return { error: error.message || error };
      }
      return { error: 'An unknown error occurred' };
    }
  }
  
}
