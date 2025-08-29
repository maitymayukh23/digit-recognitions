import { Component } from '@angular/core';

@Component({
  selector: 'app-slate',
  imports: [],
  templateUrl: './slate.html',
  styleUrl: './slate.css'
})
export class Slate {
  grid = Array.from({ length: 28 }, () => Array.from({ length: 28 }, () => 0));
  drawing = false;
  onMouseDown(row: number, col: number){
    this.drawing = true;
    this.setCell(row, col);
  }
  onMouseUp(){
    this.drawing = false;
  }
  onMouseEnter(row: number, col: number){
    if(this.drawing){
      this.setCell(row, col);
    }
  }
  setCell(row: number, col: number){
    this.grid[row][col] = 255; //white
  }
  getMatrix(){
    //return flattened grid
    return this.grid.flat();
  }
  clearGrid(){
    this.grid = Array.from({ length: 28 }, () => Array.from({ length: 28 }, () => 0));
  }

}
