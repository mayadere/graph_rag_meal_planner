async function fetchMealPlan() {
    const constraint = document.getElementById("constraint").value;
    const response = await fetch(`/api/generate-meal-plan?constraint=${constraint}`);
    const data = await response.json();
    document.getElementById("output").innerText = data.meal_plan;
}
