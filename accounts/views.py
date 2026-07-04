from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm, SkillForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Account created for {user.username}. Please log in."
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Verify credentials
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Create session and log the user in
                messages.success(request, f"Welcome back, {user.username}!")

                # Redirect to next page
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


@login_required
def profile_view(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "accounts/profile.html", context)


@login_required
def profile_edit_view(request):

    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("profile")

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/profile_edit.html", context)


@login_required
def skill_create_view(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, f'Skill "{skill.name}" added successfully.')
            return redirect("skill_list")
    else:
        form = SkillForm()
    context = {
        "form": form,
        "action": "Add",
    }
    return render(request, "accounts/skill_form.html", context)


@login_required
def skill_list_view(request):
    skills = request.user.skills.all()
    context = {
        "skills": skills,
    }
    return render(request, "accounts/skill_list.html", context)
