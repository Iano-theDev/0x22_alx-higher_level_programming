#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
}
    
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let widthHolder = this.width;
    this.width = this.height;
    this.height = widthHolder;
  }

  double () {
    this.width = this.width*2;
    this.height = this.height*2;
  }
};
