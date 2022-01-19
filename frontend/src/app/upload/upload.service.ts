import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Response } from './response';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  
  rcgFile: any;
  rclFile: any;

  constructor(private httpClient: HttpClient) { }

  updateRCLFile(newFile): void {
    this.rclFile = newFile;    
    console.log('Updated rcl file');
  }

  updateRCGFile(newFile): void {
    this.rcgFile = newFile;    
    console.log('Updated rcg file');
  }

  canUpload(): boolean { return this.rcgFile != null && this.rclFile != null; }

  postFiles(): Observable<Response>{
    const formData = new FormData();
    formData.append("rcg", this.rcgFile);
    formData.append("rcl", this.rclFile);

    console.log('Posting data');

    return this.httpClient.post<Response>("http://localhost:3000/upload", formData);
  }
}
