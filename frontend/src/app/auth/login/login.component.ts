import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  user = {
    username: '',
    password: '',
    rememberMe: false,

  }
  constructor(private router: Router) { } // Inject Router to navigate after login

  login(form: NgForm) {
    if (form.valid) {
      console.log('Login successful for user:', this.user.username);

      // Navigate to the dashboard or another route after successful login
      this.router.navigate(['/dashboard']); // Change '/dashboard' to your desired route
    } else {
      // Handle form validation errors
      console.error('Form is invalid');
    }
  }
}
