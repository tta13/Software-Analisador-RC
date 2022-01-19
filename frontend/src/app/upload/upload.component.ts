import { Component, OnInit } from '@angular/core';
import { UploadService } from './upload.service';
import { Response } from './response';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  constructor(private uploadService: UploadService) { }

  response: Response =  new Response();
  hasUploaded: boolean;
  
  
  ngOnInit(): void {
    this.hasUploaded = false;
  }
  
  onRCGFileChanged(event){
    if(event.target.files && event.target.files[0]){
      this.uploadService.updateRCGFile(event.target.files[0]);
    }
  }

  onRCLFileChanged(event){
    if(event.target.files && event.target.files[0]){
      this.uploadService.updateRCLFile(event.target.files[0]);
    }
  }

  canUpload(){
    return this.uploadService.canUpload();
  }

  submitFiles(event){
    this.hasUploaded = false;

    this.uploadService.postFiles()
      .subscribe((response: Response) => {
        this.response = response;

        if(this.response.success)
          this.hasUploaded = true;
      });
  }

  getMessage(): string {
    return this.response.msg;
  }

  successfulUpload(): boolean {
    return this.response.success;
  }
}
