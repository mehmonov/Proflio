
function app() {
    return {
        step: 1,
        hasExperience: false,
        experienceCount: 0,
        addExperience() {
            this.experienceCount++;
            const container = document.getElementById('experiences-container');
            const newExperience = document.createElement('div');
            newExperience.innerHTML = `
                <div class="mb-5 border p-4 rounded-lg shadow-sm">
                    <div class="mb-5">
                        <label class="font-bold mb-1 text-gray-700 block">Company Name</label>
                        <input type="text" name="company_${this.experienceCount}" class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none focus:shadow-outline text-gray-600 font-medium border" required>
                    </div>
                    <div class="mb-5">
                        <label class="font-bold mb-1 text-gray-700 block">Job Description</label>
                        <textarea name="job_description_${this.experienceCount}" class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none focus:shadow-outline text-gray-600 font-medium border" required></textarea>
                    </div>
                    <div class="mb-5">
                        <label class="font-bold mb-1 text-gray-700 block">Start Date</label>
                        <input type="date" name="start_date_${this.experienceCount}" class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none focus:shadow-outline text-gray-600 font-medium border" required>
                    </div>
                    <div class="mb-5">
                        <label class="font-bold mb-1 text-gray-700 block">End Date</label>
                        <input type="date" name="end_date_${this.experienceCount}" class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none focus:shadow-outline text-gray-600 font-medium border">
                    </div>
                    <div class="mb-5 flex items-center">
                        <input type="checkbox" name="currently_working_${this.experienceCount}" class="form-checkbox h-5 w-5 text-teal-600">
                        <span class="ml-2 text-gray-700">Currently Working</span>
                    </div>
                </div>
            `;
            container.appendChild(newExperience);
        }
    }
}
