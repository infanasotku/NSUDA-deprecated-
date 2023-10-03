const projectBlock = document.querySelector(".project_block");

const observer = new IntersectionObserver((entries) =>
{
    entries.forEach((entry) => {
        if (entry.isIntersecting)
        {
            projectBlock.classList.add("show");
        }
    });
});


const projectBlockTrigger = document.querySelector(".project_block_trigger");
observer.observe(projectBlockTrigger);