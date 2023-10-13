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

$(".content .skill_block ul li").hover(
    function () {
        console.log('kek');
        $(this).removeClass('out').addClass('over');
    },
    function () {
        $(this).removeClass('over').addClass('out');
    }
);

function separatorWidth()
{
    $(".content .skill_block .separator").width(
        $(".content .skill_block .ul_experience").width()
    );
}
separatorWidth();

scaleFuncs.push(separatorWidth);


