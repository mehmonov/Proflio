   

        const editUserInfoButton = document.getElementById('editUserInfo');
        const editUserInfoModal = document.getElementById('editUserInfoModal');

        editUserInfoButton.addEventListener('click', function() {
            editUserInfoModal.classList.remove('hidden');
        });

        function closeEditModal() {
            editUserInfoModal.classList.add('hidden');
        }

        // Close modal when clicking outside
        editUserInfoModal.addEventListener('click', function(e) {
            if (e.target === editUserInfoModal) {
                closeEditModal();
            }
        });

        const editSkillsButton = document.getElementById('editSkills');
        const editExperienceButton = document.getElementById('editExperience');
        const editSkillsModal = document.getElementById('editSkillsModal');
        const editExperienceModal = document.getElementById('editExperienceModal');

        editSkillsButton.addEventListener('click', function() {
            openModal('editSkillsModal');
        });

        editExperienceButton.addEventListener('click', function() {
            openModal('editExperienceModal');
        });

        function openModal(modalId) {
            document.getElementById(modalId).classList.remove('hidden');
        }

        function closeModal(modalId) {
            document.getElementById(modalId).classList.add('hidden');
        }

        // Close modals when clicking outside
        [editSkillsModal, editExperienceModal].forEach(modal => {
            modal.addEventListener('click', function(e) {
                if (e.target === modal) {
                    closeModal(modal.id);
                }
            });
        });

function changeSection(sectionName) {
	// Hide all content sections
	document.querySelectorAll('#content > section').forEach(section => {
		section.classList.add('hidden');
	});

	// Show the selected content section
	document.getElementById(`${sectionName}-content`).classList.remove('hidden');

	// Update active section styling
	document.querySelectorAll('[data-section]').forEach(el => {
		el.classList.remove('bg-blue-50', 'border-b', 'border-l-gray-100', 'border-b-blue-500', 'border-b-4');
		el.querySelector('div').classList.remove('text-blue-600');
		el.querySelector('svg').setAttribute('fill', '#5f6368');
	});

	const activeSection = document.querySelector(`[data-section="${sectionName}"]`);
	activeSection.classList.add('bg-blue-50', 'border-b', 'border-l-gray-100', 'border-b-blue-500', 'border-b-4');
	activeSection.querySelector('div').classList.add('text-blue-600');
	activeSection.querySelector('svg').setAttribute('fill', '#4880d7');
}

// Share functionality
const shareButton = document.getElementById('shareButton');
const shareModal = document.getElementById('shareModal');
const shareUrl = document.getElementById('shareUrl');

shareButton.addEventListener('click', function() {
	shareModal.classList.remove('hidden');
	shareUrl.value = window.location.href;
});

function closeShareModal() {
	shareModal.classList.add('hidden');
}

function copyShareUrl() {
	shareUrl.select();
	document.execCommand('copy');
	alert('URL copied to clipboard!');
}

function shareVia(platform) {
	const url = encodeURIComponent(window.location.href);
	const text = encodeURIComponent(document.title);
	let shareUrl;

	switch(platform) {
		case 'twitter':
			shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${text}`;
			break;
		case 'facebook':
			shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
			break;
		case 'whatsapp':
			shareUrl = `https://wa.me/?text=${text}%20${url}`;
			break;
	}

	window.open(shareUrl, '_blank');
}

// Close modal when clicking outside
shareModal.addEventListener('click', function(e) {
	if (e.target === shareModal) {
		closeShareModal();
	}
});

// Set initial active section
changeSection('facilities');

function addSkillField() {
    const container = document.getElementById('skillsContainer');
    const newField = document.createElement('div');
    newField.className = 'mb-4';
    newField.innerHTML = '<input type="text" name="skills" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">';
    container.appendChild(newField);
}

function loadCompanyDetails(selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const companyDetails = document.getElementById('companyDetails');

    if (selectedOption.value) {
        document.getElementById('companyName').value = selectedOption.dataset.name;
        document.getElementById('jobDescription').value = selectedOption.dataset.description;
        document.getElementById('startDate').value = selectedOption.dataset.startDate;
        document.getElementById('endDate').value = selectedOption.dataset.endDate || '';
        companyDetails.style.display = 'block';
    } else {
        document.getElementById('companyName').value = '';
        document.getElementById('jobDescription').value = '';
        document.getElementById('startDate').value = '';
        document.getElementById('endDate').value = '';
        companyDetails.style.display = 'none';
    }
}

const editLinksButton = document.getElementById('editLinks');
const editWebsiteStyleButton = document.getElementById('editWebsiteStyle');
const editLinksModal = document.getElementById('editLinksModal');
const editWebsiteStyleModal = document.getElementById('editWebsiteStyleModal');

editLinksButton.addEventListener('click', function() {
    document.getElementById('editLinksModal').style.display = 'block';
});

editWebsiteStyleButton.addEventListener('click', function() {
    openModal('editWebsiteStyleModal');
});

function addLinkField() {
    const container = document.getElementById('linksContainer');
    const newField = document.createElement('div');
    newField.className = 'mb-4';
    newField.innerHTML = `
        <input type="text" name="link_names" placeholder="Link Name" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
        <input type="url" name="link_urls" placeholder="URL" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
        <input type="text" name="link_colors" placeholder="Color" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
        <input type="text" name="link_icons" placeholder="Icon Class" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
    `;
    container.appendChild(newField);
}

// Close modals when clicking outside
[editLinksModal, editWebsiteStyleModal].forEach(modal => {
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal(modal.id);
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const addLinkBtn = document.getElementById('addLinkBtn');
    const linkFields = document.getElementById('linkFields');

    if (addLinkBtn) {
        addLinkBtn.addEventListener('click', addNewLinkField);
    }

    function addNewLinkField() {
        const newField = document.createElement('div');
        newField.className = 'flex items-center space-x-2 mb-4';
        newField.innerHTML = `
            <select name="link_types" class="flex-grow bg-gray-700 border border-gray-600 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500">
                <option value="">Select platform</option>
                <option value="telegram">Telegram</option>
                <option value="instagram">Instagram</option>
                <option value="facebook">Facebook</option>
                <option value="twitter">Twitter</option>
                <option value="linkedin">LinkedIn</option>
                <option value="youtube">YouTube</option>
                <option value="tiktok">TikTok</option>
                <option value="whatsapp">WhatsApp</option>
                <option value="github">GitHub</option>
                <option value="project_url">Project URL</option>
            </select>
            <input type="url" name="link_urls" placeholder="https://" class="flex-grow bg-gray-700 border border-gray-600 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500">
            <button type="button" onclick="removeLink(this)" class="px-2 py-1 bg-red-500 text-white rounded-full hover:bg-red-600">Remove</button>
        `;
        linkFields.appendChild(newField);
    }

    // Load existing links when the modal is opened
    const editLinksButton = document.getElementById('editLinks');
    if (editLinksButton) {
        editLinksButton.addEventListener('click', loadExistingLinks);
    }

    function loadExistingLinks() {
        // Clear existing fields
        linkFields.innerHTML = '';

        // Add fields for existing links
        // This is a placeholder - you'll need to replace this with actual data from your backend
        const existingLinks = [
            { type: 'telegram', url: 'https://t.me/username' },
            { type: 'instagram', url: 'https://instagram.com/username' },
            // Add more existing links here
        ];

        existingLinks.forEach(link => {
            const newField = document.createElement('div');
            newField.className = 'flex items-center space-x-2 mb-4';
            newField.innerHTML = `
                <select name="link_types" class="flex-grow bg-gray-700 border border-gray-600 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500">
                    <option value="">Select platform</option>
                    <option value="telegram" ${link.type === 'telegram' ? 'selected' : ''}>Telegram</option>
                    <option value="instagram" ${link.type === 'instagram' ? 'selected' : ''}>Instagram</option>
                    <!-- Add more options here -->
                </select>
                <input type="url" name="link_urls" value="${link.url}" class="flex-grow bg-gray-700 border border-gray-600 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500">
                <button type="button" onclick="removeLink(this)" class="px-2 py-1 bg-red-500 text-white rounded-full hover:bg-red-600">Remove</button>
            `;
            linkFields.appendChild(newField);
        });
    }
});

function removeLink(button) {
    button.closest('div').remove();
}