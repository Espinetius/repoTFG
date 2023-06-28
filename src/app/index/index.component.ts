import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-index',
    templateUrl: './index.component.html',
    styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
    @Output() indexClicked: EventEmitter<void> = new EventEmitter<void>();
    @Output() repoClicked: EventEmitter<void> = new EventEmitter<void>();
    @Output() configClicked: EventEmitter<void> = new EventEmitter<void>();

    constructor() { }
    ngOnInit(): void {

    }
    onIndex() {
        this.indexClicked.emit();
    }
    onRepos() {
        this.repoClicked.emit();
    }
    onConfig() {
        this.configClicked.emit()
    }
}
