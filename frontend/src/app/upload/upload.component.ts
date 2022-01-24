import { Component, OnInit } from '@angular/core';
import { UploadService } from './upload.service';
import { Response } from './response';
import { BehaviorSubject, Observable } from "rxjs";

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  constructor(private uploadService: UploadService) { }

  loading: BehaviorSubject<boolean> = new BehaviorSubject(false as boolean)
  response: Response =  new Response();
  hasUploaded: boolean;
  
  
  ngOnInit(): void {
    this.hasUploaded = false;
    this.uploadService.onInit();
  }
  
  onRCGFileChanged(event){
    this.hasUploaded = false;
    if(event.target.files && event.target.files[0]){
      this.uploadService.updateRCGFile(event.target.files[0]);

      const element = document.getElementById('customFileLabel-rcg');
      if(element){    
        element.innerHTML = event.target.files[0].name;
      }
    }else{      
      this.uploadService.updateRCLFile(null);

      const element = document.getElementById('customFileLabel-rcg');
      if(element)
        element.innerHTML = "Select .rcg file";
    }
  }

  onRCLFileChanged(event){
    this.hasUploaded = false;
    if(event.target.files && event.target.files[0]){
      this.uploadService.updateRCLFile(event.target.files[0]);

      const element = document.getElementById('customFileLabel-rcl');
      if(element)
        element.innerHTML = event.target.files[0].name;
    }
    else{
      this.uploadService.updateRCLFile(null);

      const element = document.getElementById('customFileLabel-rcl');
      if(element)
        element.innerHTML = "Select .rcl file";
    }
  }

  canUpload(){
    return this.uploadService.canUpload();
  }

  submitFiles(event){
		this.loading.next(true);
    this.hasUploaded = false;
    this.uploadService.postFiles()
      .subscribe({
        next: (response) => {
          this.response = response;

          this.hasUploaded = true;
			  },
			  complete: () => this.loading.next(false),      
      });
  }

  getMessage(): string {
    return this.response.msg;
  }

  successfulUpload(): boolean {
    return this.response.success;
  }

  isLoading(): Observable<boolean> {
    return this.loading.asObservable();
  }
}
